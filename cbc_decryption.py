# We are team 6
from cryptography.hazmat.primitives.ciphers import modes, Cipher, algorithms

byteEncoding = 'ascii'

# Function that adds padding to fit desired key length
def make_key(s, length):
    # print("Before:" + s + ",")
    s = s.replace("\n", "")
    
    for i in range(len(s), length):
        s += " "
    if len(s) > length:
        s = s[:length]
        
    # print("After:" + s + ",")
    return bytes(s, byteEncoding)

def applyDecryption(key, iv, ct):
    cipher = Cipher(algorithms.AES128(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(ct) + decryptor.finalize()

# Define a main function that loops through the wordsEn.txt and prints to decrypted.txt if the output countains "the" in it
def main():
    print("Starting")
    
    # Open all neccessary files
    englishWordsFile = open("wordsEn.txt", "r")
    encryptedFile = open("encrypted6.txt", "rb")
    decryptedFile = open("decrypted.txt", "wb")
    keyFile = open("key.txt", "wb")
    
    # Loop through all the possible words and attempt to decrypt it
    iv = bytes("0000000000000000", byteEncoding)
    for word in englishWordsFile.readlines():
    # word = englishWordsFile.readline()
        key = make_key(word, 16)
        decryptedOutput = applyDecryption(key, iv, encryptedFile.read())
        if decryptedOutput.count(bytes("the", byteEncoding)) > 0:
            print("Found something!")
            decryptedFile.write(decryptedOutput)
            keyFile.write(key)
        
        
    # Close all neccessary files
    englishWordsFile.close()
    encryptedFile.close()
    decryptedFile.close
    keyFile.close()
    
    print("Has Finished Decrypting")


if __name__ == "__main__":
    main()


