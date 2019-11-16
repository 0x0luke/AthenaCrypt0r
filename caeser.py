#Taken from https://stackoverflow.com/questions/8886947/caesar-cipher-function-in-python
#Modified for assignment

def caesar(plainText, shift): 
  cipherText = ""
  for ch in plainText:
    if ch.isalpha():
      stayInAlphabet = ord(ch) + shift 
      if stayInAlphabet > ord('z'):
        stayInAlphabet -= 26
      finalLetter = chr(stayInAlphabet)
      cipherText += finalLetter
  #print "Your ciphertext is: ", cipherText
  return cipherText