import sys, socket


def open(ip, port):
    s = socket.socket()
    try:
        res = s.connect((ip, port))
        print(res)
        return True
    except:
        return False


def scan(ip, portlist):
    for x in portlist:
        if open(ip, x):
            print("%s host %s port is open" % (ip, x))
        else:
            print("%s host %s port close" % (ip, x))


def rscan(ip, s, e):
    for x in range(s, e):
        if open(ip, x):
            print("%s host %s port open" % (ip, x))
        else:
            print("%s host %s port close" % (ip, x))


def main():
    defaultport = [22, 80, 135, 139, 445, 1433, 3306, 3389, 5944]
    str = sys.argv[1]
    if len(sys.argv) == 2:
        if str[0] == '-':
            option = sys.argv[1][1:]
            if option == 'version':
                print("软件版本是1.0")
            elif option == 'help':
                print("目前没有help，你sos都没用")
            sys.exit()
        scan(sys.argv[1], defaultport)
    elif len(sys.argv) == 3:
        if ',' in sys.argv[2]:
            p = sys.argv[2]
            p = p.split(',')
            a = []
            for x in p:
                a.append(int(x))
            scan(sys.argv[1], a)
        elif '-' in sys.argv[2]:
            a = sys.argv[2]
            a = a.split('-')
            s = int(a[0])
            e = int(a[1])
            rscan(sys.argv[1], s, e)
        pass


if __name__ == '__main__':
    main()
