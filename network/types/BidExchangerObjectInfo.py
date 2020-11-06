import network.utils.CustomDataWrapper as dataWrapper # pylint: disable=import-error
from misc import * # pylint: disable=unused-wildcard-import

class Type:
    name = 'BidExchangerObjectInfo'

    def __init__(self):
        self.objectUID = 0
        self.objectGID = 0
        self.objectName = ''
        self.objectType = 0
        self.effects = []
        self.prices = []

    def __str__(self):
        return \
        '\tobjectUID: ' + str(self.objectUID) + '\n' \
        '\tobjectGID: ' + str(self.objectGID) + '\n' \
        '\tobjectName: ' + str(self.objectName) + '\n' \
        '\tobjectType: ' + str(self.objectType) + '\n' \
        '\teffects: ' + ', '.join(str(effect) for effect in self.effects) + '\n' \
        '\tprices:\n\t- ' + '\n\t- '.join(str(price) for price in self.prices) + '\n'

    def deserialize(self, data):
        self.objectUID, data = dataWrapper.readVarInt(data)
        self.objectGID, data = dataWrapper.readVarShort(data)
        self.objectName = getObjectName(self.objectGID) # pylint: disable=undefined-variable
        self.objectType, data = dataWrapper.readInt(data)
        effectsLen, data = dataWrapper.readShort(data)
        for _ in range(0, effectsLen):
            effect, data = dataWrapper.readShort(data)
            self.effects.append(effect)
        pricesLen, data = dataWrapper.readShort(data)
        for _ in range(0, pricesLen):
            price, data = dataWrapper.readVarLong(data)
            self.prices.append(price)
        return data