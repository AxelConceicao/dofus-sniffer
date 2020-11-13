from sniffer import Sniffer
from protocolBuilder import ProtocolBuilder
from CustomDataWrapper import Data, Buffer
from misc import * # pylint: disable=unused-wildcard-import
import sys

class Test:
    def __init__(self):
        self.id = 5722
        self.data = Data([5, 0, 40, 105, 111, 112, 32, 50, 48, 48, 32, 99, 104, 101, 114, 99, 104, 101, 32, 103, 117, 105, 108, 100, 101, 32, 97, 108, 108, 105, 97, 110, 99, 101, 32, 116, 104, 111, 114, 32, 115, 118, 112, 95, 173, 209, 43, 0, 8, 53, 111, 50, 57, 121, 109, 49, 114, 66, 37, 45, 70, 1, 154, 0, 0, 0, 7, 66, 97, 98, 121, 108, 111, 110, 0, 0, 3, 6, 35, 97])

def action(msg):
    if msg.id != 5722 : return
    content = protocolBuilder.build(msg.id, msg.data)
    print(content)
    # print(', '.join(str(c) for c in msg.data.data))

if __name__ == "__main__":
    protocolBuilder = ProtocolBuilder()
    Sniffer(action)
    # action(Test()) # testmode
    exit(0)