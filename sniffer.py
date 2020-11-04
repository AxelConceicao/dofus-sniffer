from scapy.all import * # pylint: disable=unused-wildcard-import
from dofus_packet import DofusPacket

class Sniffer:
    PORT = 5555
    filter = 'tcp src port ' + str(PORT)

    def __init__(self, callback):
        self.callback = callback
        sniff(prn=self.handle, filter=self.filter)

    def handle(self, pkt):
        if Raw in pkt:
            data = pkt[Raw].load
            while len(data):
                dofusPacket = DofusPacket()
                data = dofusPacket.parse(data)
                self.callback(dofusPacket)