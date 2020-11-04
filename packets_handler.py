from packets import *

class PacketsHandler:
    protocol = None
    messages = {
        'ChatServerMessage': ChatServerMessage.Packet, # pylint: disable=undefined-variable
    }

    def __init__(self, protocol):
        self.protocol = protocol

    def deserialize(self, dofusPacket):
        for packet in self.protocol['messages']:
            if packet['protocolID'] == dofusPacket.protocolID:
                if packet['name'] in self.messages:
                    self.messages[packet['name']](dofusPacket).deserialize()
                else:
                    print('No support for "' + packet['name'] + '" packet (' + str(packet['protocolID']) + ')')
                return
        print('No support for "' + str(packet['protocolID']) + '" packet')
        