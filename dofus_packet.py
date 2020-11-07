from network.utils.CustomDataWrapper import * # pylint: disable=unused-wildcard-import

class DofusPacket:

    def __init__(self):
        self.protocolID = 0
        self.lenType = 0
        self.messageLen = 0
        self.messageData = None

    def printDebug(self):
        print('ProtocolID: ' + str(self.protocolID))
        print('LenType: ' + str(self.lenType))
        print('MessageLen: ' + str(self.messageLen))
        print(' '.join(str(c) for c in self.messageData))
        
    def parse(self, data):
        header = int.from_bytes(data[0:2], byteorder="big")
        self.protocolID = header >> 2
        self.lenType = header & 3
        self.messageLen = int.from_bytes(data[2:2 + self.lenType], byteorder="big")
        self.messageData = CustomDataWrapper(data[2 + self.lenType:2 + self.lenType + self.messageLen])
        return data[2 + self.lenType + self.messageLen:]