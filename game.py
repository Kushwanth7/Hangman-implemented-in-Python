# @author Kushwanth
# 
# Hangman game


import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    line = inFile.readline()
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist


def chooseWord(wordlist):
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    for c in lettersGuessed:
        if (c in secretWord):
            continue
        else:
            return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    tempStr = ""
    for c in secretWord:
        if c in lettersGuessed:
            tempStr = tempStr + c
        else:
            tempStr = tempStr + "_ "
    return tempStr



def getAvailableLetters(lettersGuessed):
    x = string.ascii_lowercase
    for c in lettersGuessed:
        if c in x:
            x = x.replace(c,"")
    return x
    

def hangman(secretWord):    
    print "Welcome to the game, Hangman!\n"
    print "I am thinking of a word that is " + str(len(secretWord)) + " long\n"

    guessCount = 10
    availableLetters = string.ascii_lowercase
    list = []
    while(guessCount > 0):
        print "-------------"
        print "You have " + str(guessCount) + " left\n"
        print "Available letters: " + availableLetters + "\n"
        letterEntered =  raw_input("Please guess a letter: ")
        if letterEntered not in availableLetters or len(letterEntered) > 1:
            print "Oops! You've already guessed that letter or the entered input is more than one character in length or you have not enetered a letter present in the English alphabet : " + getGuessedWord(secretWord,list)
            continue
        list.append(letterEntered)
        output = isWordGuessed(secretWord,list)
        if(output == True):
            print "Good guess: " + getGuessedWord(secretWord,list)
            if("_" not in getGuessedWord(secretWord, list)):
                print "-------------"
                print "Congratulations, you won!"
                exit(0)
            availableLetters = availableLetters.replace(letterEntered, "")
        else:
            guessCount -= 1
            print "Oops! That letter is not in my word: " + getGuessedWord(secretWord,list)
            list.remove(letterEntered)
    print "-----------"
    print "Sorry, you ran out of guesses. The word was " + secretWord        



wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)