from sniffer import Sniffer
from packets_handler import PacketsHandler
from dofus_packet import DofusPacket
from misc import * # pylint: disable=unused-wildcard-import
import json
import sys

PROTOCOL_FILENAME = 'json/protocol.json'

if __name__ == "__main__":
    debug = False
    if len(sys.argv) > 1 and sys.argv[1] in ['-d', '-D', '--debug']:
        debug = True
    if isFileExist(PROTOCOL_FILENAME):
        with open(PROTOCOL_FILENAME, 'r') as json_file:
            protocol = json.load(json_file)
    else:
        exit(1)
    packetHandler = PacketsHandler(protocol, debug)
    Sniffer(packetHandler.deserialize)
    exit(0)