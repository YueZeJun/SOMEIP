import SOMEIP

if __name__ == "__main__":
    sender = SOMEIP.Sender({"ip": "192.168.67.65", "port": 30490, "iface": "vEthernet"},
                      {"ip": "192.168.67.65", "port": 30490}, "udp")

    # build someip packet
    sip = SOMEIP.SOMEIP()
    sip.msg_id.srv_id = 0xffff
    sip.msg_id.sub_id = 0x1
    sip.msg_id.event_id = 0x0110
    sip.req_id.client_id = 0xdead
    sip.req_id.session_id = 0xbeef
    sip.msg_type = 0x02
    sip.retcode = 0x00
    sip.add_payload(b"payloadDemo")

    # send message
    sender.send(sip)




