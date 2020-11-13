from scapy.all import sniff, Raw, IP # pylint: disable=no-name-in-module
from colorama import Fore, Back, Style
from CustomDataWrapper import Data, Buffer

class Msg():
    def __init__(self, buffer):
        self.b = True
        try:
            if len(buffer) == 32:
                buffer.pos = 0
                self.b = False
                raise ValueError
            header = int.from_bytes(buffer.read(2), byteorder="big")
            self.id = header >> 2
            self.lenType = header & 3
            self.dataLen = int.from_bytes(buffer.read(self.lenType), byteorder="big")
            # print('dataLen: ' + str(self.dataLen))
            self.data = Data(buffer.read(self.dataLen))
        except (IndexError, ValueError):
            buffer.pos = 0
            self.b = False
        else:
            buffer.end()

    def __bool__(self):
        return self.b

class Sniffer:
    def __init__(self, callback):
        self.callback = callback
        self.buffer = Buffer()
        sniff(filter='tcp src port 5555', lfilter = lambda pkt: pkt.haslayer(Raw), prn = lambda pkt: self.receive(pkt))

    def receive(self, pkt):
        # print()
        # print('bufferSize: ' + str(len(self.buffer.data)))
        # print('pktLen: ' + str(len(pkt.getlayer(Raw))))
        # print(pkt.getlayer(IP).id)
        if self.buffer.lastPktID and pkt.getlayer(IP).id < self.buffer.lastPktID:
            print(Fore.RED + 'Ahead packet !' + Style.RESET_ALL)
            self.buffer.preadd(bytes(pkt.getlayer(Raw)))
        else:
            self.buffer += bytes(pkt.getlayer(Raw))
            self.buffer.lastPktID = pkt.getlayer(IP).id
        # print('bufferSize APRES: ' + str(len(self.buffer.data)))
        msg = Msg(self.buffer)
        while msg:
            # print('ID: ' + str(msg.id) + ' - dataLen: ' + str(len(msg.data)))
            # print(' '.join(str(c) for c in msg.data.data))
            # print(' '.join(f"{c:08b}" for c in msg.data.data))
            self.callback(msg)
            msg = Msg(self.buffer)