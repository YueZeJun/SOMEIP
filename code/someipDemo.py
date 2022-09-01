from collections import namedtuple
from scapy.all import *
from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether

import SOMEIP_Protocol

iface = namedtuple('iface', 'name ip port')
ETH_IFACE = iface(name='enp0s3', ip='10.0.2.15', port=30490)

# build SOME/IP packet
sip = SOMEIP_Protocol.SOMEIP()
sip.msg_id.srv_id = 0xffff
sip.msg_id.sub_id = 0x1
sip.msg_id.event_id = 0x0110

sip.req_id.client_id = 0xdead
sip.req_id.session_id = 0xbeef

sip.msg_type = 0x02
sip.retcode = 0x00
# sip.add_payload("hello")

# send message
p = Ether() / IP(src='10.0.2.15', dst='10.0.2.14') / UDP(sport=30490, dport=30490) / sip
p.show()

sendp(p, iface=ETH_IFACE.name)

print(p.haslayer(SOMEIP_Protocol.SOMEIP))
print(p.getlayer(SOMEIP_Protocol.SOMEIP))
c = SOMEIP_Protocol.SOMEIP(raw(p.getlayer(SOMEIP_Protocol.SOMEIP)))
c.show()
print(c)
