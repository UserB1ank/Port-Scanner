import optparse

from socket import *
from threading import Thread, RLock

screenLock = RLock()


# 扫描器
def connScan(tgtHost, tgtPort):
    connSkt = socket(AF_INET, SOCK_STREAM)
    #
    try:
        s = connSkt.connect((tgtHost, tgtPort))
        try:
            connSkt.send('HAHA'.encode('utf-8'))
            results = connSkt.recv(1024)
            reply = f"[+] {tgtPort}/tcp open " + results.decode('utf-8').replace('\n', '')
            print(reply)
        except:
            print("[+] %d/tcp open " % tgtPort)
            pass
        print('\n')
    except:
        pass
    finally:
        connSkt.close()


# 过渡函数
def Scan(tgtHost, tgtPorts):
    # try:
    #     tgtIP = gethostbyname(tgtHost)
    # except:
    #     print("[-] Cannot resolve '%s': Unknown host" % tgtHost)
    #     return
    # try:
    #     tgtName = gethostbyaddr(tgtIP)
    #     print("\n[+] Scan Results For: " + tgtName[0])
    # except:
    #     print("\n[+] Scan Results for:" + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
    return


def main():
    parser = optparse.OptionParser()
    parser.add_option('-H', dest='tgtHost', type='string',
                      help='specify target host')
    parser.add_option('-p', dest='tgtPort', type='string',
                      help='specify target port[s] separated by comma')
    options, args = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = options.tgtPort
    if tgtHost is None:
        print("[-] You must specify a target host")
        exit(0)
    if tgtPorts is None:  # 默认扫描前1000个端口
        tgtPorts = range(1, 1001)
        Scan(tgtHost, tgtPorts)
        pass
    if '-' in tgtPorts:
        tgtRange = str(tgtPorts).split('-')
        tgtPorts = range(int(tgtRange[0]), int(tgtRange[1]) + 1)
        Scan(tgtHost, tgtPorts)
    if ',' in tgtPorts:
        tgtPorts = str(tgtPorts).split(',')
        Scan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
