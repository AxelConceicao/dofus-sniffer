class DofusPacket:
    protocolID = None
    lengthType = None
    messageLength = None
    messageData = None

    def __init__(self):
        pass

    def __str__(self):
        return \
        'ProtocolID: ' + str(self.protocolID) + \
        ' - LengthType: ' + str(self.lengthType) + \
        ' - MessageLength: ' + str(self.messageLength) + \
        '\n' + ' '.join(str(c) for c in self.messageData) + '\n'
        
    def parse(self, data):
        header = int.from_bytes(data[0:2], byteorder="big")
        self.protocolID = header >> 2
        self.lengthType = header & 3
        self.messageLength = int.from_bytes(data[2:2 + self.lengthType], byteorder="big")
        self.messageData = data[2 + self.lengthType:2 + self.lengthType + self.messageLength]
        return data[2 + self.lengthType + self.messageLength:]