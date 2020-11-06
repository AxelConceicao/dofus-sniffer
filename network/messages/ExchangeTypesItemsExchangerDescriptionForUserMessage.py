import network.utils.CustomDataWrapper as dataWrapper # pylint: disable=import-error
import network.types.BidExchangerObjectInfo as BidExchangerObjectInfo # pylint: disable=import-error

class Message:
    name = 'ExchangeTypesItemsExchangerDescriptionForUserMessage'

    def __init__(self, dofusPacket, protocol):
        self.dofusPacket = dofusPacket
        self.protocol = protocol
        self.objectType = 0
        self.objects = []

    def printMessage(self):
        print(self.name + ' (' + str(self.dofusPacket.protocolID) + ')')
        print('- objectType: ' + str(self.objectType))
        for item in self.objects:
            print(str(item))

    def deserialize(self):
        data = self.dofusPacket.messageData
        self.objectType, data = dataWrapper.readInt(data)
        objectsLen, data = dataWrapper.readShort(data)
        for _ in range(0, objectsLen):
            obj = BidExchangerObjectInfo.Type()
            data = obj.deserialize(data)
            self.objects.append(obj)
        self.printMessage()
        if len(data) == 0:
            print('Packet successfully deserialized!')
        else:
            print('Deserialization has encountered an error.')