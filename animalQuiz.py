"""
Author: Zoe Mitchell
Consulted: 
Date: 02/16/22
Purpose: CS111 ps04
Filename: animalQuiz.py
"""

def boolFromResponse(string):
    '''
    this function takes a string, makes it lowercase,
    and then returns True if it begins with 'y'.
    '''
    lowerString = string.lower()
    return lowerString.startswith('y')

def boolFromUser(prompt):
    '''
    this function gets an answer from user input and passes
    it through the boolFromResponse function to get True if
    the user's input started with a 'y'.
    '''
    answer = input(prompt)
    return boolFromResponse(answer)

def chooseAnimal(isMeat, isCold, isFuzzy):
    '''
    this function takes three parameters to determine which
    animal should be returned depending on whether the arguments
    are true/false.
    '''
    if isMeat == True:
        if isCold == True:
            if isFuzzy == True:
                return 'polar bear'
            else:
                return 'orca'
        elif isCold == False and isFuzzy == True:
            return 'tiger'
        else:
            return 'komodo dragon'
    
    if isMeat == False:
        if isCold == False:
            if isFuzzy == False:
                return 'tortoise'
            else:
                return 'bunny'
        elif isCold == True and isFuzzy == False:
            return 'clam'   
        else:
            return 'yak'
        
def animalQuiz():
    '''
    this function takes no parameters and instead prompts the user
    for three yes/no answers to questions. Using the above functions
    it decides what animal the user is based on the input.
    '''
    print("What animal are you? Let's find out!")
    meatQ = 'Do you like to eat meat? '
    coldQ = 'Do you like cold weather? '
    fuzzyQ = 'Do you like fuzzy things? '
    
    result = chooseAnimal(boolFromUser(meatQ), boolFromUser(coldQ), boolFromUser(fuzzyQ))
    
    print(' ')
    print('Your animal is the ' + result)
        
        
        
        
        
         