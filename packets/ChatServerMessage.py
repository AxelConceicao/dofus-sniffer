# from packets.DofusPacket import DofusPacket
from datetime import datetime
import packets.unpack_types as unpack

class ChatServerMessage:
    name = 'ChatServerMessage'
    channel = None
    content = None
    timestamp = None
    fingerprint = None
    senderId = None
    senderName = None
    prefix = None
    senderAccountId = None

    def __init__(self, dofusPacket, protocol):
        self.dofusPacket = dofusPacket
        self.protocol = protocol

    def __str__(self):
        return \
        self.name + ' (' + str(self.dofusPacket.protocolID) + ')\n' + \
        'Channel: ' + self.channel + '\n' + \
        'Message: ' + self.content + '\n' + \
        'Time: ' + datetime.fromtimestamp(self.timestamp).strftime('%H:%M:%S') + '\n' + \
        'SenderName: ' + self.senderName + '\n'

    def deserialize(self):
        # print(str(self.dofusPacket))
        data = self.dofusPacket.messageData
        unpackedData, data = unpack.fromByte(data)
        for enum in self.protocol['enumerations']:
            if enum['name'] == 'ChatActivableChannelsEnum':
                self.channel = list(enum['members'].keys())[list(enum['members'].values()).index(str(unpackedData))]
        self.content, data = unpack.fromString(data)
        self.timestamp, data = unpack.fromInt(data)
        self.fingerprint, data = unpack.fromString(data)
        self.senderId, data = unpack.fromDouble(data)
        self.senderName, data = unpack.fromString(data)
        self.prefix, data = unpack.fromString(data)
        self.senderAccountId, data = unpack.fromInt(data)
        if len(data) == 0:
            print(str(self))
            # print('Packet successfully deserialized!')
        else:
            print('Deserialization has encountered an error.')