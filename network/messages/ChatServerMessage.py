from datetime import datetime

class Message:
    name = 'ChatServerMessage'
    channelName = ''

    def __init__(self, protocol, channel = 0, content = '', timestamp = 0, fingerprint = '', senderId = '', senderName = '', prefix = '', senderAccountId = 0):
        self.protocol = protocol
        self.channel = channel
        self.content = content
        self.timestamp = timestamp
        self.fingerprint = fingerprint
        self.senderId = senderId
        self.senderName = senderName
        self.prefix = prefix
        self.senderAccountId = senderAccountId

    def printMessage(self):
        print('Channel: ' + str(self.channel) + ' (' + self.channelName + ')')
        print('Time: ' + str(self.timestamp) + ' (' + datetime.fromtimestamp(self.timestamp).strftime('%H:%M:%S') + ')')
        print('Message: ' + self.content)
        print('SenderName: ' + self.senderName)

    def deserialize(self, _input):
        self.channel = int.from_bytes(_input.readByte(), byteorder='big')
        for enum in self.protocol['enumerations']:
            if enum['name'] == 'ChatActivableChannelsEnum':
                self.channelName = list(enum['members'].keys())[list(enum['members'].values()).index(str(self.channel))]
        self.content = _input.readUTF()
        self.timestamp = _input.readInt()
        self.fingerprint = _input.readUTF()
        self.senderId = _input.readDouble()
        self.senderName = _input.readUTF()
        self.prefix = _input.readUTF()
        self.senderAccountId = _input.readInt()
        if _input.isDeserialized():
            self.printMessage()
            # print('Packet successfully deserialized!')
        else:
            print('Deserialization has encountered an error.')