from scapy.all import sniff, Raw, IP, ICMP # pylint: disable=no-name-in-module
from colorama import Fore, Back, Style
from CustomDataWrapper import Data, Buffer
from Misc import * # pylint: disable=unused-wildcard-import

class Msg():
    def __init__(self, buffer, protocol):
        self.b = True
        self.protocol = protocol
        self.error = ''
        try:
            header = int.from_bytes(buffer.read(2), byteorder="big")
            self.id = header >> 2
            self.lenType = header & 3
            self.dataLen = int.from_bytes(buffer.read(self.lenType), byteorder="big")
            self.checkHeader()
            print('dataLen: ' + str(self.dataLen))
            self.data = Data(buffer.read(self.dataLen))
        except IndexError:
            buffer.pos = 0
            self.b = False
        except ValueError:
            eprint(self.error)
            buffer.pos = 0
            self.b = False
        else:
            buffer.end()

    def checkHeader(self):
        if not next((item for item in self.protocol['messages'] if item['protocolID'] == self.id), None):
            self.error = 'Could not find message with id: "' + str(self.id) + '"'
            raise ValueError
        elif not self.lenType in [0, 1, 2, 3]:
            self.error = 'Wrong lenType "' + str(self.lenType) + '"'
            raise ValueError

    def __bool__(self):
        return self.b

class Sniffer:
    def __init__(self, callback, protocol):
        self.callback = callback
        self.protocol = protocol
        self.buffer = Buffer()
        self.lastPkt = None
        sniff(filter='tcp src port 5555', lfilter = lambda pkt: pkt.haslayer(Raw), prn = lambda pkt: self.receive(pkt))

    def receive(self, pkt):
        print('--')
        print('bufferSize: ' + str(len(self.buffer.data)))
        print('pktLen: ' + str(len(pkt.getlayer(Raw))))
        print(pkt.getlayer(IP).id)
        if self.lastPkt and pkt.getlayer(IP).src != self.lastPkt.getlayer(IP).src:
            self.lastPkt = None
            # self.buffer = Buffer()
            wprint('Source changed!')
        if self.lastPkt and pkt.getlayer(IP).id < self.lastPkt.getlayer(IP).id:
            eprint('Late packet!')
            self.buffer.reorder(bytes(pkt.getlayer(Raw)), len(self.lastPkt.getlayer(Raw)))
        else:
            self.buffer += bytes(pkt.getlayer(Raw))
        print('bufferSize APRES: ' + str(len(self.buffer.data)))
        self.lastPkt = pkt
        msg = Msg(self.buffer, self.protocol)
        while msg:
            print('ID: ' + str(msg.id) + ' - dataLen: ' + str(len(msg.data)))
            # print(' '.join(str(c) for c in msg.data.data))
            # print(' '.join(f"{c:08b}" for c in msg.data.data))
            self.callback(msg)
            msg = Msg(self.buffer, self.protocol)