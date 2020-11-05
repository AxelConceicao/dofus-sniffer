import array

def fromByte(data):
    return data[0], data[1:]

def fromString(data):
    length = int.from_bytes(data[:2], byteorder='big')
    unpackedData = array.array('b', data[2:length + 2]).tostring().decode('utf-8') # •_•
    return unpackedData, data[length + 2:]

def fromInt(data):
    return int.from_bytes(data[:4], byteorder='big'), data[4:]

def fromDouble(data):
    return int.from_bytes(data[:8], byteorder='big'), data[8:]