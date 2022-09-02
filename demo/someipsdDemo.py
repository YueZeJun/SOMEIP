
import SOMEIP

if __name__ == "__main__":
    sender = SOMEIP.Sender({"ip": "192.168.67.65", "port": 30490, "iface": "vEthernet"},
                      {"ip": "192.168.67.65", "port": 30490}, "udp")

    # build someipsd packet
    sdp = SOMEIP.SD()

    sdp.flags = 0x00
    # add the entry_array
    sdp.entry_array = [
        SOMEIP.SDEntry_EventGroup(srv_id=0x1234, n_opt_1=1, inst_id=0x1234, major_ver=0x03, eventgroup_id=0x04, cnt=0x0,
                           ttl=0x05),
        SOMEIP.SDEntry_Service(srv_id=0x4321, index_1=1, n_opt_1=1, inst_id=0x4321, major_ver=0x03, minor_ver=0x1,
                        ttl=0x04)]
    # add the option_array
    sdp.option_array = [
        SOMEIP.SDOption_IP4_EndPoint(addr="192.168.0.1", l4_proto=0x11, port=0xd903),
        SOMEIP.SDOption_IP6_EndPoint(addr="ff88::8888:8888:8888:8888", l4_proto=0x11, port=0x0201)]

    sender.send(sdp)




