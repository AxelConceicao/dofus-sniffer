import array

def readByte(data):
    return data[0], data[1:]

def readShort(data):
    return int.from_bytes(data[:2], byteorder='big'), data[2:]

def readInt(data):
    return int.from_bytes(data[:4], byteorder='big'), data[4:]

def readDouble(data):
    return int.from_bytes(data[:8], byteorder='big'), data[8:]

def readUTF(data):
    len = int.from_bytes(data[:2], byteorder='big')
    unpackedData = array.array('b', data[2:len + 2]).tostring().decode('utf-8') # •_•
    return unpackedData, data[len + 2:]

def readVarShort(data):
    value = 0
    offset = 0
    while offset < 16:
        b, data = readByte(data)
        hasNext = (b & 128) == 128
        if offset > 0:
            value += (b & 127) << offset
        else:
            value += b & 127
        offset += 7
        if not hasNext:
            return value, data
    return 0, data

def readVarLong(data):
    value = 0
    offset = 0
    while offset < 64:
        b, data = readByte(data)
        hasNext = (b & 128) == 128
        if offset > 0:
            value += (b & 127) << offset
        else:
            value += b & 127
        offset += 7
        if not hasNext:
            return value, data
    return 0, data

def readVarInt(data):
    value = 0
    offset = 0
    while offset < 32:
        b, data = readByte(data)
        hasNext = (b & 128) == 128
        if offset > 0:
            value += (b & 127) << offset
        else:
            value += b & 127
        offset += 7
        if not hasNext:
            return value, data
    return 0, data