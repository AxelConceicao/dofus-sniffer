from misc import * # pylint: disable=unused-wildcard-import

class Type:
    name = 'BidExchangerObjectInfo'

    def __init__(self, objectUID = 0, objectGID = 0, objectType = 0, effects = None, prices = None):
        self.objectUID = objectUID
        self.objectGID = objectGID
        self.objectType = objectType
        self.effects = effects
        self.prices = prices

    def deserialize(self, _input):
        self.effects = []
        self.prices = []
        self.objectUID = _input.readVarInt()
        self.objectGID = _input.readVarShort()
        self.objectType = _input.readInt()
        effectsLen = _input.readShort()
        for _ in range(0, effectsLen):
            self.effects.append(_input.readShort())
        pricesLen = _input.readShort()
        for _ in range(0, pricesLen):
            self.prices.append(_input.readVarLong())
        return _input