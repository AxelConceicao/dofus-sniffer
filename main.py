from sniffer import Sniffer
from packets_handler import PacketsHandler
from dofus_packet import DofusPacket
import json
import errno
import sys
import os

PROTOCOL_FILENAME = 'protocol.json'

def isFileExist(file):
    if not os.path.isfile(file): 
        print("No such file : " + file, file=sys.stderr)
        exit(1)
    return True

if __name__ == "__main__":
    if isFileExist(PROTOCOL_FILENAME):
        with open(PROTOCOL_FILENAME, 'r') as json_file:
            protocol = json.load(json_file)
    packetHandler = PacketsHandler(protocol)
    Sniffer(packetHandler.deserialize)
    exit(0)