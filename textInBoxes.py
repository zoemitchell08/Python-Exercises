"""
Authors: Zoe Mitchell
Consulted:
Date: 02/08/22
Purpose: CS111 ps02
"""

def boxIt(string, symbol):
    """boxIt takes two arguments (a message and a symbol) and
    prints the message with a box made up of the symbol around it"""
    
    stringLen = len(string) 
    print(symbol * (stringLen + 12))
    print(symbol + '     ' + string + '     ' + symbol)
    print(symbol * (stringLen + 12))
        
        
def marginBox(string, symbol, margin):
    """marginBox takes three arguments and prints the same thing as boxIt
    BUT it prints a box with a margin of the third argument"""
    
    middleLine = symbol + (' ' * margin) + string + (' ' * margin) + symbol 
    midLen = len(middleLine)
    print(symbol * midLen)
    print(middleLine)
    print(symbol * midLen)
    
def customBox():
    """customBox calls marginBox but the arguments come from user input
    and become the customization of the box size/look and the message inside it"""
    
    customString = input('What is your message? ')
    customSymbol = input('What border should we use (1 letter only)? ')
    customMargin = int(input("How big should the margin be (an integer)? "))
    marginBox(customString, customSymbol, customMargin)
    
    
    
def doubleBox(top, btm, symbol, margin):
    """doubleBox takes four arguments to create a box with two lines of text inside it
    right now there is an error and the output does not account for the difference between length in strings"""
    bigWord = max(len(top), len(btm))#stores the length of the longer word
    smallWord = min(len(top), len(btm))#stores the length of the shorter word
    wordDiff = bigWord - smallWord #stores the diff in length btwn the words
    longBorder = symbol * (bigWord + (margin * 2 + 2)) #stores the size of the top/bottom border
    
    if len(top) == len(btm):
        topLine = symbol + (' ' * margin) + top + (' ' * margin) + symbol
        btmLine = symbol + (' ' * margin) + btm + (' ' * (margin)) + symbol
        print(longBorder)
        print(topLine)
        print(btmLine)
        print(longBorder)
        
    if len(top) > len(btm):
        topLine = symbol + (' ' * margin) + top + (' ' * margin) + symbol
        btmLine = symbol + (' ' * (margin + (wordDiff - 1))) + btm + (' ' * (margin + (wordDiff - 1))) + symbol
        print(longBorder)
        print(topLine)
        print(btmLine)
        print(longBorder)
        
    if len(top) < len(btm):
        topLine = symbol + (' ' * (margin + wordDiff)) + top + (' ' * (margin + wordDiff)) + symbol
        btmLine = symbol + (' ' * margin) + btm + (' ' * margin) + symbol
        print(longBorder)
        print(topLine)
        print(btmLine)
        print(longBorder)
    
doubleBox('hi', 'b', '*', 3)