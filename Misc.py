import os
import sys
import json
import errno
from colorama import Fore, Back, Style

def eprint(msg):
    print(Fore.RED + msg + Style.RESET_ALL, file=sys.stderr)

def wprint(msg):
    print(Fore.YELLOW + msg + Style.RESET_ALL)

def sprint(msg):
    print(Fore.GREEN + msg + Style.RESET_ALL)

def isFileExist(filename):
    if not os.path.isfile(filename): 
        eprint("No such file : " + filename)
        raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), filename)
    return True