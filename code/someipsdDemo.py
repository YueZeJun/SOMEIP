from collections import namedtuple
from scapy.all import *
from collections import namedtuple

from scapy.layers.inet import IP, UDP
from scapy.layers.l2 import Ether
# import sys
# sys.path.append("..")

from SOMEIP_SD_Protocol import *
from scapy.all import *

iface = namedtuple('iface', 'name ip port')
ETH_IFACE_A = iface(name='enp0s3', ip='10.0.2.15', port=30490)
ETH_IFACE_B = iface(name='enp0s3', ip='10.0.2.14', port=30490)
# 发送方式 srp1 sendp

sdp = SD()

sdp.flags = 0x00
sdp.entry_array = [
    SDEntry_EventGroup(srv_id=0x1111, n_opt_1=1, inst_id=0x2222, major_ver=0x03, eventgroup_id=0x04, cnt=0x0,
                          ttl=0x05)]
sdp.option_array = [
    SDOption_IP4_EndPoint(addr="192.168.0.1", l4_proto=0x11, port=0xd903)]

# build request and reply packages
p = Ether() / IP(src=ETH_IFACE_A.ip, dst=ETH_IFACE_B.ip) / UDP(sport=ETH_IFACE_A.port,
                                                               dport=ETH_IFACE_B.port) / sdp.getSomeip(True)
r = Ether() / IP(src=ETH_IFACE_B.ip, dst=ETH_IFACE_A.ip) / UDP(sport=ETH_IFACE_B.port,
                                                               dport=ETH_IFACE_A.port) / sdp.getSomeip(True)
r['SD'].entry_array[0].type = SDEntry_EventGroup.TYPE_EVTGRP_SUBSCRIBE_ACK

sendp(p, iface=ETH_IFACE_A.name)
