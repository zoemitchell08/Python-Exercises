"""
Authors:
Consulted:
Date:
Purpose: wordGuesser task: Allows user to guess words and reveals
  which letters are correct (or misplaced but present).
"""

import random # will be used to play a game with a random word

#---------------#
# Provided Text #
#---------------#

# This variable has the text you'll need to print out at the start of
# each game, so you don't have to type it all in yourself. It's put in
# all-caps to indicate that it's a global variable: any function can use
# it, but it cannot be modified inside a function.
INTRO = """\
Welcome to guess-that-word!
You will guess what the word could be and we will reveal which letters
of your guess are correct. If a letter is in the word but in a different
location, we'll let you know.

'@' means this letter is correct.
'*' means this letter is present in a different spot.
'-' means this letter is not present.

Use the hints to guess the word!
"""


#----------------------#
# Write your code here #
#----------------------#
def letterHints(hiddenWord, guess):
    '''
    given a word guess from the user, this function returns hints for each
    letter in the form of '-', '*', and '@' to show if the letter is a
    good guess or not
    '''
    hint = ''
    index = 0
    for index in range(len(guess)):
        letter = guess[index]
        if letter in hiddenWord:
            if letter in hiddenWord[index]:
                hint += '@'
            elif letter in hiddenWord:
                hint += '*'
        else:
            hint += '-'
        index = index + 1
    return hint


def getGuess(length):
    '''
    this function takes a length of a string and asks for a user input.
    if the user input matches the length of the string, then their guess
    is returned
    '''
    guess = input('Guess a word (' + str(length) + ' letters): ')
    while len(guess) != length:
        print('You must guess a word with ' +  str(length) + ' letters.')
        guess = input('Guess a word (' + str(length) + ' letters): ')
    return guess

def playGame(hiddenWord):
    '''
    this function takes a hidden word and prompts the user
    for their guess (using getGuess). if the guess is not right, it calls
    letterHints and repeats until they guess correctly. There are
    different messages depending on the number of guesses it took.
    '''
    print(INTRO)
    print('The word has ' + str(len(hiddenWord)) + ' letters.')
    guess = getGuess(len(hiddenWord))
    guessCount = 1
    while guess != hiddenWord:
        hint = letterHints(hiddenWord, guess)
        print(hint)
        guess = getGuess(len(hiddenWord))
        guessCount += 1
    
    if guess == hiddenWord:
        print('Congratulations! You guessed it, the word was: ' + hiddenWord)
        if guessCount == 1:
            print('Wow, you guessed it in one try!')
        elif guessCount in range(1, 8):
            print('Great job! You guessed the word in just ' + str(guessCount) + ' tries.')
        else:
            print('You guessed the word in ' + str(guessCount) + ' tries.')
        
        
          
#--------------#
# Random Games #
#--------------#

# This variable holds a list of words that we will use to pick a random
# word to play the game with. The list is not very long, so we don't
# use it to validate guesses. The words are all between 4 and 7 letters
# long, and most of them are drawn from the index of our textbook, or
# otherwise relate to computer science concepts. There are three words
# that start with each letter of the alphabet, except for 'x', 'y', and
# 'z'.
WORDS = [
    "assign", "alias", "append", "branch", "binary", "boolean",
    "catch", "comment", "copy", "data", "debug", "declare",
    "element", "error", "empty", "file", "float", "format",
    "global", "game", "grid", "hash", "header", "heap",
    "input", "integer", "iterate", "join", "joule", "jump",
    "keyword", "kernel", "keys", "loop", "list", "local",
    "mutable", "method", "module", "none", "newline", "nested",
    "object", "open", "order", "python", "print", "pattern",
    "quote", "queue", "quine", "range", "return", "recurse",
    "syntax", "string", "shell", "test", "tuple", "turtle",
    "update", "unique", "user", "value", "void", "virtual",
    "while", "wave", "word", "xerox", "yield", "zero", "zombie"
]


# Note: This won't work until you've finished playGame.

def playRandomGame():
    """
    Works like playGame, except the word is chosen randomly from the
    WORDS list. Use this to play a game where you don't know the answer
    ahead of time.
    """
    playGame(random.choice(WORDS))
