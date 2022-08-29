from collections import namedtuple
from scapy.all import *
from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether

import SOMEIP as someip

iface = namedtuple('iface', 'name ip port')
ETH_IFACE = iface(name='WLAN 2', ip='192.168.31.11', port=30490)

# build SOME/IP packet
sip = someip.SOMEIP()
sip.msg_id.srv_id = 0xffff
sip.msg_id.sub_id = 0x1
sip.msg_id.event_id = 0x0110

sip.req_id.client_id = 0xdead
sip.req_id.session_id = 0xbeef

sip.msg_type = 0x02
sip.retcode = 0x00
sip.add_payload(b"hello")

# send message
p = Ether() / IP(src='192.168.31.11', dst='192.168.31.230') / TCP(sport=30490, dport=30490) / sip
p.show()

sendp(p, iface=ETH_IFACE.name)

print(p.haslayer(someip.SOMEIP))
print(p.getlayer(someip.SOMEIP))
c = someip.SOMEIP(raw(p.getlayer(someip.SOMEIP)))
c.show()
print(c)

