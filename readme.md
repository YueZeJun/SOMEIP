SOMEIP
======
*****************************************************************************************
概述：<br>
		支持 SOME/IP 数据包的发送、接收并解析<br>
		使用它你可以发送任何你想要的someip/someipsd 数据包<br>
		复制到你的python环境的Lib\site-packages目录下，然后就可以直接在代码中'import SOMEIP'并使用了<br>
<br>
Overview：<br>
		Supports sending, receiving and parsing of SOME/IP packets<br>
		With it you can send any someip/someipsd packets you wanted<br>
		Copy it to the Lib\site-packages directory of your python environment, then you can directly import the library to use<br>
*****************************************************************************************
如下是项目的层级结构/Below is the project structure：<br>
|->bin<br>
&emsp;&emsp;|->protocol<br>
&emsp;&emsp;&emsp;&emsp;|->SOMEIP.py 		&emsp;&emsp;&emsp;&emsp;SOME/IP 类消息定义|SOME/IP class message definition<br>
&emsp;&emsp;&emsp;&emsp;|->SOMEIP_SD.py         &emsp;&emsp;&emsp;SOME/IP-SD 类消息定义|SOME/IP-SD class message definition<br>
&emsp;&emsp;|->transceiver<br>
&emsp;&emsp;&emsp;&emsp;|->sender.py             &emsp;&emsp;发送器|Send someip/someipsd packets<br>
&emsp;&emsp;&emsp;&emsp;|->sniffer.py            &emsp;&emsp;监听器|Monitor, parse and deliver someip/someipsd packets<br>
|->demo<br>
&emsp;&emsp;|->snifferDemo.py            		&emsp;&emsp;监听器监听someip/someipsd报文|Use sniffer to listen to someip/someipsd<br>
&emsp;&emsp;|->someipDemo.py             		&emsp;&emsp;发送器发送someip报文|Use sender to send someip packets<br>
&emsp;&emsp;|->someipsdDemo.py           		&emsp;&emsp;发送器发送someipsd报文|Use sender to send someipsd packets<br>
|->docs                          			&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;官方文档|Official documentation<br>
|->notebook                      			&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;关键流程图以及总结的思维导图|Relevant flowcharts and mind maps<br>
*****************************************************************************************
参考代码/Reference Code：<br>
https://github.com/jamores/eth-scapy-someip<br>

参考文档/Reference documentation：<br>
AUTOSAR_TR_SomeIpExample_4.2.1.pdf<br>
AUTOSAR_PRS_SOMEIPServiceDiscoveryProtocol.pdf<br>
AUTOSAR_PRS_SOMEIPProtocol.pdf<br>
*****************************************************************************************
editor:YueZeJun<br>
email:sir.yue@qq.com<br>

[qrcode]!(https://github.com/YueZeJun/SOMEIP/blob/dev/QRcode.png)
