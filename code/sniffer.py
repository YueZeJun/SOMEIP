import SOMEIP_Protocol as SOMEIP
from SOMEIP_SD_Protocol import SD
from scapy.all import *
import queue


class SOMEIPSniffer(object):
    def __init__(self, netName: str, filter: str, queue: queue.Queue):
        """
        Listen for SOMEIP/SOMEIPSD messages and expose them to users after parsing
        :param netName: NIC name
        :param filter: BPF filter to apply
        :param queue:
        """
        self.queue = queue
        self.sniffer = AsyncSniffer(iface=netName, filter=filter, prn=self.guess_payload_class, count=0)
        self.sniffer.start()

    def stop(self):
        """
        Stop listening for SOMEIP/SOMEIPSD messages
        :return:
        """
        if self.sniffer.running:
            self.sniffer.stop(False)

    def __del__(self):
        self.stop()

    def guess_payload_class(self, packet):
        sd_header = b"\xff\xff\x81\x00"
        raw_data = raw(packet.getlayer(scapy.packet.Raw))
        if raw_data[:4] == sd_header:
            #todo 需要增加option 判断
            last_layer = SD(raw_data)
        else:
            last_layer = SOMEIP.SOMEIP(raw_data)
        # last_layer.show()
        self.queue.put(last_layer)


#
# ifacestr = "enp0s3"  # 网口名称，这里要换成自己的网卡名称
# filterstr = "udp port 30490"  # 过滤条件，为空表示不限制
# sniff(filter=None, prn=print_packet, iface=ifacestr, count=0)

if __name__ == "__main__":
    queueObj = queue.Queue()

    A = SOMEIPSniffer("enp0s3", "udp port 30490", queueObj)
    while True:
        time.sleep(1)
        if not queueObj.empty():
            print("=====================")
            resp = queueObj.get()
            print(resp.layers())
            resp.show()
