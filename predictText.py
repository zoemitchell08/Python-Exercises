# -*- coding: utf-8 -*-
"""
Authors:
Consulted:
Date:
Purpose: predictText task: Based on observed words, predict the next
    word that will be typed.
"""

import random


#-----------------------------#
# Provided code (DO NOT EDIT) #
#-----------------------------#

def chooseRandomly(options):
    """
    Accepts a sequence of options and returns a random option from that
    sequence. Note: you MUST use this function to pick random words in
    your code below, otherwise your assignment will not be graded
    properly.
    """
    return random.choice(list(options))


#----------------------#
# Write your code here #
#----------------------#

#--------#
# Part A #
#--------#

def buildPredictions(words):
    """
    this functino takes in a list of strings and returns a
    prediction dictionary in the following format:
        {
        "she": [ "said", "was" ],
        "said": [ "that" ]
        "that": [ "she" ]
        "was": [ "tired" ]
        }
    the dictionary should be all lowercase. If given an empty
    list, it will return an empty dictionary.
    """
    library = {}
    for string in range(len(words) - 1):
        word = words[string].lower()
        if word not in library:
            library[word] = [words[string + 1]]
        else:
            library[word].append(words[string + 1]) 
            
    return library
    
#--------#
# Part B #
#--------#

def predictText(startWord, howMany, predictions, policy):
    """
    this function takes the first word of a text, a number for
    how many words to add after the first, a dictionary using the
    buildPredictions function (which will have at least one key with
    at least one value, see example below):
    
        predictions = buildPredictions([ "ONE", "two", "one", "three" ])
    
    and a policy for what word to choose from
    a key with more than one value.
    
    It will return a string with the starting word and a number
    (howMany) of words each based on the one before.
    
    If a word is chosen that has no previous word in the dictionary,
    then the function will pick from a list of the keys using the
    same policy that keys with multiple values uses.
    
    The startword will always be provided in lowercase.
    """    
    string = [startWord.lower()]
          
    for i in range(howMany):
        if string[i] in predictions:
            if policy == 'first':
                guess = (predictions[string[i]])[0]
                string.append(guess)
            elif policy == 'last':
                guess = (predictions[string[i]])[-1]
                string.append(guess)
            else:
                guess = chooseRandomly(string[i])
        else:
            guess = list(predictions.keys())
            string.append(chooseRandomly(guess))
     
    return string
        
'''
just something to think about:
for key, value in sorted(predictions.items()):
    if len([item for item in value if item]) > 1:
        print('multiple')
        string.append(predictions[policy])
     else:
        print('just one')
        string.append(predictions[policy])
'''
