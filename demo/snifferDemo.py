import SOMEIP
import queue


if __name__ == "__main__":
    queueObj = queue.Queue()

    ifacestr = "enp0s3"  # Network port name, you need to change this variable to your own network card name
    filterstr = "udp port 30490"  # BPF filter to apply (Please make sure that only someip or someipsd packets exist after filtering)

    sniffer = SOMEIP.Sniffer(ifacestr, filterstr, queueObj)
    while True:
        if not queueObj.empty():
            print("=================================")
            resp = queueObj.get()
            # print the detail of the resp
            resp.show()
            print("=================================")

