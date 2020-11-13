import os
import sys
import json
from colorama import Fore, Back, Style

OBJECTS_FILENAME = 'json/objects.json'

def eprint(msg):
    print(Fore.RED + msg + Style.RESET_ALL, file=sys.stderr)

def wprint(msg):
    print(Fore.YELLOW + msg + Style.RESET_ALL)

def sprint(msg):
    print(Fore.GREEN + msg + Style.RESET_ALL)

def isFileExist(file):
    if not os.path.isfile(file): 
        eprint("No such file : " + file)
    return True