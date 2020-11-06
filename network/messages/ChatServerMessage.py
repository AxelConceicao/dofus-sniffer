import network.utils.CustomDataWrapper as dataWrapper # pylint: disable=import-error
from datetime import datetime

class Message:
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

    def printMessage(self):
        print(self.name + ' (' + str(self.dofusPacket.protocolID) + ')')
        print('Channel: ' + self.channel)
        print('Time: ' + datetime.fromtimestamp(self.timestamp).strftime('%H:%M:%S'))
        print('Message: ' + self.content)
        print('SenderName: ' + self.senderName)

    def deserialize(self):
        data = self.dofusPacket.messageData
        unpackedData, data = dataWrapper.readByte(data)
        for enum in self.protocol['enumerations']:
            if enum['name'] == 'ChatActivableChannelsEnum':
                self.channel = list(enum['members'].keys())[list(enum['members'].values()).index(str(unpackedData))]
        self.content, data = dataWrapper.readUTF(data)
        self.timestamp, data = dataWrapper.readInt(data)
        self.fingerprint, data = dataWrapper.readUTF(data)
        self.senderId, data = dataWrapper.readDouble(data)
        self.senderName, data = dataWrapper.readUTF(data)
        self.prefix, data = dataWrapper.readUTF(data)
        self.senderAccountId, data = dataWrapper.readInt(data)
        if len(data) == 0:
            self.printMessage()
            # print('Packet successfully deserialized!')
        else:
            print('Deserialization has encountered an error.')