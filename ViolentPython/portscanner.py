# portscanner.py
# Get hostname and list comma separated ports.
# Translate hostname into IPv4 address using sockets.gethostbyname(hostname)
# Connect each port in the given list to the target address
# send garbage data to port, then analyze banner results.


from socket import *
from optparse import OptionParser


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        print("[+] {0}/tcp open".format(tgtPort))
        print("[+] {0}".format(str(results)))
        connSkt.close()
    except:
        print("[-] {0}/tcp closed".format(tgtPort))


def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print("[-] Cannot resolve {0}: unknown host".format(tgtHost))
        return

    try:
        tgtName = gethostbyaddr(tgtIP)
        print("\n[+] Scan Results for: {0}".format(tgtName[0]))
    except:
        print("\n[+] Scan results for: {0}".format(tgtIP))

    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print("Scanning port {0}".format(tgtPort))
        connScan(tgtHost, int(tgtPort))


def main():
    parser = OptionParser('usage prog -H' +
                          '<target host> -p <target port>')

    parser.add_option('-H',
                      dest='tgtHost',
                      type='string',
                      help='specificy target host')

    parser.add_option('-p',
                      dest='tgtPort',
                      type='string',
                      help='Specifiy target port')

    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')

    if (tgtHost == None) | (tgtPorts == None):
        print(parser.usage)
        exit(0)

    portScan(tgtHost, tgtPorts)


if __name__ in ['__console__', '__main__']:
    main()
