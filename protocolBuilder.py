from misc import * # pylint: disable=unused-wildcard-import

PROTOCOL_FILENAME = 'json/protocol.json'

class ProtocolBuilder:
    protocol = None
    content = None
    data = None
    methods = None

    def __init__(self):
        if isFileExist(PROTOCOL_FILENAME):
            with open(PROTOCOL_FILENAME, 'r') as json_file:
                self.protocol = json.load(json_file)
        if self.protocol:
            sprint('Protocol loaded')
        else:
            eprint('Unable to load protocol')
            exit(1)

    def getMessageUsingID(self, ID):
        return next(item for item in self.protocol['messages'] if item["protocolID"] == ID)

    def getMessageUsingName(self, name):
        return next(item for item in self.protocol['messages'] if item["name"] == name)

    def deserializeField(self, msg, field):
        # print(field['name'])
        return self.methods[field['write_method']]()

    def builder(self, msg):
        content = {}
        if msg['super_serialize']:
            content = self.builder(self.getMessageUsingName(msg['super']))
        # print('- ' + msg['super'])
        content[msg['name']] = {}
        for pos in range(0, len(msg['fields'])):
            field = next(item for item in msg['fields'] if item["position"] == pos)
            content[msg['name']][field['name']] = self.deserializeField(msg, field)
        return content

    def build(self, ID, data):
        self.content = {}
        self.data = data
        self.setMethods()
        self.content = self.builder(self.getMessageUsingID(ID))
        print('--')
        return self.content

    def setMethods(self):
        self.methods = {
            'writeByte': self.data.readByte,
            'writeShort': self.data.readShort,
            'writeInt': self.data.readInt,
            'writeDouble': self.data.readDouble,
            'writeUTF': self.data.readUTF,
        }
