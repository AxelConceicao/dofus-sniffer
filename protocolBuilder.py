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

    def getObjectByID(self, ID):
        for objectType in ['messages', 'types']:
            obj = next((item for item in self.protocol[objectType] if item["protocolID"] == ID), None)
            if obj : return obj
        eprint('Unable to get object with ID "' + str(ID) + '"')
        exit(1)

    def getObjectByName(self, name):
        for objectType in ['messages', 'types']:
            obj = next((item for item in self.protocol[objectType] if item["name"] == name), None)
            if obj : return obj
        eprint('Unable to get object with name "' + str(name) + '"')
        exit(1)

    def deserializeField(self, obj, field):
        if 'is_vector' in field:
            vector = []
            for _ in range(0, self.methods[field['write_length_method']]()):
                if 'type_namespace' in field:
                    if 'prefixed_by_type_id' in field:
                        vector.append(self.deserializeObject(self.getObjectByID(self.methods[field['write_type_id_method']]())))
                    else:
                        vector.append(self.deserializeObject(self.getObjectByName(field['type'])))
                else:
                    vector.append(self.methods[field['write_method']]())
            return vector
        else:
            if 'type_namespace' in field:
                if 'prefixed_by_type_id' in field:
                    return self.deserializeObject(self.getObjectByID(self.methods[field['write_type_id_method']]()))
                else:
                    return self.deserializeObject(self.getObjectByName(field['type']))
            else:
                return self.methods[field['write_method']]()

    def deserializeObject(self, obj):
        content = {}
        if obj['super_serialize']:
            content = self.deserializeObject(self.getObjectByName(obj['super']))
        content[obj['name']] = {}
        for pos in range(0, len(obj['fields'])):
            field = next(item for item in obj['fields'] if item["position"] == pos)
            content[obj['name']][field['name']] = self.deserializeField(obj, field)
        return content

    def build(self, ID, data):
        self.content = {}
        self.data = data
        self.setMethods()
        try:
            self.content = self.deserializeObject(self.getObjectByID(ID))
        except KeyError:
            eprint('Unable to deserialize message "' + str(ID) + '"')
            print(', '.join(str(c) for c in data.data))
        return self.content

    def setMethods(self):
        self.methods = {
            'writeByte': self.data.readByte,
            'writeShort': self.data.readShort,
            'writeInt': self.data.readInt,
            'writeDouble': self.data.readDouble,
            'writeUTF': self.data.readUTF,
            'writeVarInt': self.data.readVarInt,
            'writeVarShort': self.data.readVarShort,
            'writeVarLong': self.data.readVarLong,
            'writeBoolean': self.data.readBoolean,
            'writeFloat': self.data.readFloat
        }
