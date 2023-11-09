# We are team 6
from cryptography.hazmat.primitives.ciphers import modes, Cipher, algorithms


# Function that adds padding to fit desired key length
def add_padding(s, length):
    for i in range(len(s), length):
        s += " "
    return s

def applyDecryption(key, iv, ct):
    cipher = Cipher(algorithms.AES128(key), modes.CBC(iv))
    decryptor = cipher.decryptor()
    return decryptor.update(ct) + decryptor.finalize()

# Define a main function that loops through the wordsEn.txt and prints to decrypted.txt if the output countains "the" in it
def main():
    print("Starting")
    
    # Open all neccessary files
    englishWordsFile = open("wordsEn.txt", "r")
    encryptedFile = open("encrypted6.txt", "r")
    decryptedFile = open("decrypted.txt", "w")
    keyFile = open("key.txt", "w")
    
    # Loop through all the possible words and attempt to decrypt it
    iv = "0000000000000000"
    # for word in englishWordsFile.readlines():
    word = englishWordsFile.readline()
    key = add_padding(word, 16)
    decryptedOutput = applyDecryption(key, iv, encryptedFile.readlines())
    if decryptedOutput.count("the") > 0:
        decryptedFile.write("OUTPUT HERE")
        keyFile.write(key)
        
        
    # Close all neccessary files
    englishWordsFile.close()
    encryptedFile.close()
    decryptedFile.close
    keyFile.close()
    
    print("Has Finished Decrypting")


if __name__ == "__main__":
    main()


