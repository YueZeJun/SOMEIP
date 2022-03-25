from collections import namedtuple
from scapy.all import *
from scapy import *

import SOMEIP as someip

iface = namedtuple('iface', 'name ip port')
ETH_IFACE_A = iface(name='eth1.10', ip='169.254.179.243', port=30490)
ETH_IFACE_B = iface(name='以太网', ip='169.254.133.197', port=30490)

# build SOME/IP packet
sip = someip.SOMEIP()
sip.msg_id.srv_id = 0xffff
sip.msg_id.sub_id = 0x0
sip.msg_id.method_id = 0x0000

sip.req_id.client_id = 0xdead
sip.req_id.session_id = 0xbeef

sip.msg_type = 0x01
sip.retcode = 0x00

# send message
p = Ether() / IP(src='169.254.133.197', dst='169.254.179.243') / UDP(sport=30490, dport=30490) / sip

sendp(p, iface=ETH_IFACE_B.name)
