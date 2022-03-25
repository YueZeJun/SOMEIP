SOMEIP
|->code(代码区)
    |->SOMEIP.py        SOME/IP类消息定义
    |->SOMEIP_SD.py     SOME/IP-SD类消息定义
|->docs(官方文档)
|->notebook(相关流程图以及我总结的逻辑思维导图)
|->resource(参考源代码)

该项目基于github project:eth-scapy-someip
根据最新的autosar协议更新修复了部分bug，并增加了大量的注解用于辅助理解

注意：当前仅支持SOME/IP包的发送接受，没有针对传输层、应用层的逻辑实现

=================================================================
参考代码：
https://github.com/jamores/eth-scapy-someip
-----------------------------------------------------------------
参考文档：
AUTOSAR_TR_SomeIpExample_4.2.1.pdf
AUTOSAR_PRS_SOMEIPServiceDiscoveryProtocol.pdf
AUTOSAR_PRS_SOMEIPProtocol.pdf
=================================================================