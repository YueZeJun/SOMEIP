from ..protocol import SOMEIP
from ..protocol import SOMEIP_SD
from scapy.all import *
import queue



class Sniffer(object):
    def __init__(self, netName: str, filter: str, queue: queue.Queue):
        """
        Listen for SOMEIP/SOMEIPSD messages and expose them to users after parsing
        :param netName: NIC name
        :param filter: BPF filter to apply (Please make sure that only someip or someipsd packets exist after filtering)
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
            last_layer = SOMEIP.SOMEIP(raw_data[:16])/SOMEIP_SD.SD(raw_data[16:])
        else:
            last_layer = SOMEIP.SOMEIP(raw_data)
        # last_layer.show()
        self.queue.put(last_layer)




