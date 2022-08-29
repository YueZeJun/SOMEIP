import sys
import psutil
import SOMEIP as someip
from SOMEIP_SD import SD
import scapy
# print(sys.platform)
#
# info = psutil.net_if_addrs()
# print(info)
# for i in info:
#     print(i)
#
#     for tmp in info[i]:
#         print(tmp)
#         # print(tmp["address"])
#         print(tmp.address)


from scapy.all import *


def print_packet(packet):
    # print(packet.show())
    # print(packet.layers())
    # packet.show()
    sdHeader = b"\xff\xff\x81\x00"
    rawData = raw(packet.getlayer(scapy.packet.Raw))
    if rawData[:4] == sdHeader:
        lastLayer = SD(rawData)
    else:
        lastLayer = someip.SOMEIP(rawData)
    lastLayer.show()



ifacestr = "WLAN 2"  # 网口名称，这里要换成自己的网卡名称
filterstr = "udp port 30490"  # 过滤条件，为空表示不限制
sniff(filter=filterstr, prn=print_packet, iface=ifacestr, count=0)
