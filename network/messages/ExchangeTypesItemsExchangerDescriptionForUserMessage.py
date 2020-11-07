import network.types.BidExchangerObjectInfo as BidExchangerObjectInfo # pylint: disable=import-error
from misc import * # pylint: disable=unused-wildcard-import

class Message:
    name = 'ExchangeTypesItemsExchangerDescriptionForUserMessage'

    def __init__(self, protocol, objectType = 0, objects = None):
        self.protocol = protocol
        self.objectType = objectType
        self.objects = objects

    def printMessage(self):
        print('objectType: ' + str(self.objectType))
        for obj in self.objects:
            print()
            print('objectUID: ' + str(obj.objectUID))
            print('objectGID: ' + str(obj.objectGID) + ' (' + getObjectName(obj.objectGID) + ')') # pylint: disable=undefined-variable
            print('objectType: ' + str(obj.objectType))
            print('prices: ' + ', '.join(str(p) for p in obj.prices))

    def deserialize(self, _input):
        self.objects = []
        self.objectType = _input.readInt()
        objectsLen = _input.readShort()
        for _ in range(0, objectsLen):
            obj = BidExchangerObjectInfo.Type()
            obj.deserialize(_input)
            self.objects.append(obj)
        if _input.isDeserialized():
            self.printMessage()
            # print('Packet successfully deserialized!')
        else:
            print('Deserialization has encountered an error.')