from network.messages import *

class PacketsHandler:
    protocol = None
    debug = None
    messages = {
        'ChatServerMessage': ChatServerMessage.Message, # pylint: disable=undefined-variable
        'ExchangeTypesItemsExchangerDescriptionForUserMessage': ExchangeTypesItemsExchangerDescriptionForUserMessage.Message, # pylint: disable=undefined-variable
    }

    def __init__(self, protocol, debug):
        self.protocol = protocol
        self.debug = debug

    def printDebug(self, dofusPacket):
        print(' '.join(str(c) for c in dofusPacket.messageData.data))
        print(' '.join(f"{c:08b}" for c in dofusPacket.messageData.data))

    def deserialize(self, dofusPacket):
        # if dofusPacket.protocolID in [5722, 4275, 8712, 1111, 5009, 2994, 9281]:
        #     return
        for packet in self.protocol['messages']:
            if packet['protocolID'] == dofusPacket.protocolID:
                if self.debug : self.printDebug(dofusPacket)
                if packet['name'] in self.messages:
                    print(packet['name'] + ' (' + str(packet['protocolID']) + ')')
                    self.messages[packet['name']](self.protocol).deserialize(dofusPacket.messageData)
                else:
                    print('No support for "' + packet['name'] + '" packet (' + str(packet['protocolID']) + ')')
                print()
                return
        print('No support for "' + str(packet['protocolID']) + '" packet\n')
        