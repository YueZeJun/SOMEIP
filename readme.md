#SOMEIP

#######=========================================================================================
###概述：
#######支持 SOME/IP 数据包的发送、接收并解析
#######使用它你可以发送任何你想要的someip/someipsd 数据包
#######复制到你的python环境的Lib\site-packages目录下，然后就可以直接在代码中'import SOMEIP'并使用了
#######----------------------------------------------------------------------------------------
###Overview：
#######Supports sending, receiving and parsing of SOME/IP packets
#######With it you can send any someip/someipsd packets you wanted
#######Copy it to the Lib\site-packages directory of your python environment, then you can directly import the library to use
#######=========================================================================================
###如下是项目的层级结构/Below is the project structure：
#######|->bin
#######    |->protocol
#######        |->SOMEIP.py            SOME/IP 类消息定义                       SOME/IP class message definition
#######        |->SOMEIP_SD.py         SOME/IP-SD 类消息定义                    SOME/IP-SD class message definition
#######    |->transceiver
#######        |->sender.py            发送器                                  Send someip/someipsd packets
#######        |->sniffer.py           监听器                                  Monitor, parse and deliver someip/someipsd packets
#######|->demo
#######    |->snifferDemo.py           演示如何使用监听器监听someip/someipsd报文   Demonstrates how to use a listener to listen for someip/someipsd packets
#######    |->someipDemo.py            演示如何使用发送器发送someip报文            Demonstrate how to use the sender to send someip packets
#######    |->someipsdDemo.py          演示如何使用发送器发送someipsd报文          Demonstrate how to use the sender to send someipsd packets
#######|->docs                         官方文档                                 Official documentation
#######|->notebook                     关键流程图以及总结的思维导图                 Relevant flowcharts and mind maps I summarized
#######=========================================================================================
###参考代码/Reference Code：
#######https://github.com/jamores/eth-scapy-someip
#######-----------------------------------------------------------------------------------------
###参考文档/Reference documentation：
#######AUTOSAR_TR_SomeIpExample_4.2.1.pdf
#######AUTOSAR_PRS_SOMEIPServiceDiscoveryProtocol.pdf
#######AUTOSAR_PRS_SOMEIPProtocol.pdf
#######=========================================================================================
#######editor:YueZeJun
#######email:sir.yue@qq.com
