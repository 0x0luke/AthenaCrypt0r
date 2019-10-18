import getdirs
import os
import modify
import hashlib as h
import random as r
import time as t

def generateKey():
    keyName = "\x43\x72\x79\x70\x74\x30\x72" #Cypt0r in hexString
    salt = map(ord, keyName) # run KeyName through the ord function, set the value to salt
    r.seed(int(t.time()+r.randint(1,1337))) # generate a peusdo random seed for random
    key = h.pbkdf2_hmac('sha512', bytes(r.randint(1, 65500)), bytes(salt), r.randint(30000,60000)) # generate the encryption key - SHA512 salted, ran over a random amount of times
    encryptionKey = key.hex() # dump the key

    return encryptionKey #return it to the main function


def main(encryptionKey):

    key = encryptionKey

    return 0


if __name__=="__main__":
    main(generateKey())