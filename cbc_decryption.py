# We are team 6
from cryptography.hazmat import *

# Function that adds padding
def add_padding(s, length):
    print(length - len(s))
    print(len(s))
    for i in range(length - len(s), length):
        s += " "
    return s
    

# Define a function that takes an output and key and nicely outputs it onto decrypted.txt


# Define a main function that loops through the wordsEn.txt and prints to decrypted.txt if the output countains "the" in it
def main():
    print("Starting")
    englishWordsFile = open("wordsEn.txt", "r")
    # for word in englishWordsFile.readlines():
    word = englishWordsFile.readline()
    word = add_padding(word, 16)
    print(len(word))
    
    englishWordsFile.close()


if __name__ == "__main__":
    main()


