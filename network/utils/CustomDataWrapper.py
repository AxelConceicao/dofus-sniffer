import array

class CustomDataWrapper:
    def __init__(self, data):
        self.data = data
        self.offset = 0

    def isDeserialized(self):
        return self.offset == len(self.data)

    def readBytes(self, length):
        toRead = self.data[self.offset:self.offset + length]
        self.offset += length
        return toRead

    def readByte(self):
        return self.readBytes(1)

    def readShort(self):
        return int.from_bytes(self.readBytes(2), byteorder='big')

    def readInt(self):
        return int.from_bytes(self.readBytes(4), byteorder='big')

    def readDouble(self):
        return int.from_bytes(self.readBytes(8), byteorder='big')

    def readUTF(self):
        stringLen = self.readShort()
        return array.array('b', self.readBytes(stringLen)).tostring().decode('utf-8') # •_•

    def readVarShort(self):
        value = 0
        offset = 0
        while offset < 16:
            b = int.from_bytes(self.readByte(), byteorder='big')
            hasNext = (b & 128) == 128
            if offset > 0:
                value += (b & 127) << offset
            else:
                value += b & 127
            offset += 7
            if not hasNext:
                return value
        return 0

    def readVarLong(self):
        value = 0
        offset = 0
        while offset < 64:
            b = int.from_bytes(self.readByte(), byteorder='big')
            hasNext = (b & 128) == 128
            if offset > 0:
                value += (b & 127) << offset
            else:
                value += b & 127
            offset += 7
            if not hasNext:
                return value
        return 0

    def readVarInt(self):
        value = 0
        offset = 0
        while offset < 32:
            b = int.from_bytes(self.readByte(), byteorder='big')
            hasNext = (b & 128) == 128
            if offset > 0:
                value += (b & 127) << offset
            else:
                value += b & 127
            offset += 7
            if not hasNext:
                return value
        return 0