# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/Users/EchoTeam/Code/6.00x/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i = 0    
    while i < len(secretWord):
        for char in secretWord:
            if char not in lettersGuessed:
                return False    
                break
            i += 1
    return True
    


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''    
    for char in secretWord:
        if char not in lettersGuessed:
            secretWord = secretWord.replace(char, ' _ ') 
    return secretWord




def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    
    for char in lettersGuessed:
        if char in alpha:
            alpha = alpha.replace(char, '')
    return alpha
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    mistakesMade = 0
    lettersGuessed = []
    print ("Welcome to the game, Hangman!")
    print ("I am thinking of a word that is " +str(len(secretWord))+" letters long.")
    print ("-------------")
    
    while mistakesMade < 8:
        if isWordGuessed(secretWord, lettersGuessed):
            return ('Congratulations, you won!')            
        print ("You have "+str(8-mistakesMade)+" guesses left." )
        print ("Available letters: " +str(getAvailableLetters(lettersGuessed)))
        guess = raw_input('Please guess a letter: ').lower()

        if guess in lettersGuessed:
            print ("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
            print ("-------------")                       
        elif guess in secretWord: 
            lettersGuessed.append(guess)               
            print ("Good guess: " + str(getGuessedWord(secretWord, lettersGuessed)))
            print ("-------------")
        else:
            lettersGuessed.append(guess) 
            mistakesMade += 1
            print ("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
            print ("-------------")
    
    return ('Sorry, you ran out of guesses. The word was '+ str(secretWord) + '.')    
        
            
        
        
        
        
    
    
    






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
