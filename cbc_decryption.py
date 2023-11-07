# We are team 6
from cryptography.hazmat import *

# Function that adds padding
def add_padding(s, length):
    for i in range(len(s), length):
        s += " "
    return s
    

# Define a function that takes an output and key and nicely outputs it onto decrypted.txt


# Define a main function that loops through the wordsEn.txt and prints to decrypted.txt if the output countains "the" in it
def main():
    print("Starting")
    englishWordsFile = open("wordsEn.txt", "r")
    iv = "0000000000000000"
    
    for word in englishWordsFile.readlines():
    # word = englishWordsFile.readline()
        key = add_padding(word, 16)
        
    
    englishWordsFile.close()
    cipher = Cipher(algoritgms.AES(key), modes.CBC(iv))
    decryptor = cipher.decryptor()


if __name__ == "__main__":
    main()


