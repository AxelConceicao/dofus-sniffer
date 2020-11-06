import os
import sys
import json

OBJECTS_FILENAME = 'json/objects.json'

def isFileExist(file):
    if not os.path.isfile(file): 
        print("No such file : " + file, file=sys.stderr)
    return True

def getObjectName(objectGID):
    if not isFileExist(OBJECTS_FILENAME):
        return
    with open(OBJECTS_FILENAME, 'r', encoding="utf8") as json_file:
            objects = json.load(json_file)
            return objects[str(objectGID)]
    print('Cannot find object with GID: ' + str(objectGID), file=sys.stderr)
    return None