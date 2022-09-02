from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether
from scapy.all import *
from ..protocol import SOMEIP
from ..protocol import SOMEIP_SD


class Sender:
    def __init__(self, src: dict, dst: dict, protocol: str):
        """
        Used to set the three layers below someip or someipsd
        :param src:This dictionary must contain the keys 'ip', 'port','iface'(the interface to send the packets on)
        :param dst:This dictionary must contain the keys 'ip', 'port'
        :param protocol: 'udp' or 'tcp'
        """
        self.initFlag = 0
        self.src = src
        self.dst = dst
        self.protocol = protocol
        self._build_l3_layer()
        self.initFlag = 1

    @property
    def src(self):
        return self._src

    @src.setter
    def src(self, value: dict):
        if "ip" not in value or "port" not in value:
            raise ValueError("key missing 'ip' or 'port'")
        if "iface" not in value:
            raise ValueError("key missing 'iface'")
        self._src = value
        if self.initFlag:
            self._build_l3_layer()

    @property
    def dst(self):
        return self._dst

    @dst.setter
    def dst(self, value: dict):
        if "ip" not in value or "port" not in value:
            raise ValueError("key missing 'ip' or 'port'")
        self._dst = value
        if self.initFlag:
            self._build_l3_layer()

    @property
    def protocol(self):
        return self._protocol

    @protocol.setter
    def protocol(self, value: str):
        if value.lower() == "udp" or value.lower() == "tcp":
            self._protocol = value.lower()
        else:
            raise ValueError("protocol must be tcp or udp")
        if self.initFlag:
            self._build_l3_layer()

    def _build_l3_layer(self):
        if self.protocol == "udp":
            self.l3Layer = Ether() / IP(src=self.src["ip"], dst=self.dst["ip"]) / UDP(sport=self.src["port"],
                                                                                      dport=self.dst["port"])
        else:
            self.l3Layer = Ether() / IP(src=self.src["ip"], dst=self.dst["ip"]) / TCP(sport=self.src["port"],
                                                                                      dport=self.dst["port"])

    def send(self, package, flag=True):
        """
        Send the someip or someipsd
        :param package:
        :param flag:
        :return:
        """
        if type(package) == SOMEIP_SD.SD:
            package = package.getSomeip(flag)
        sendp(self.l3Layer/package, iface=self.src["iface"])


