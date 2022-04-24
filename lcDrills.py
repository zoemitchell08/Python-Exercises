"""
Authors: Peter Mawhorter
Consulted:
Date: 2022-3-25
Purpose: lcDrills task: practice with list comprehensions.
"""

import os


# Convert each function that uses a loop into a function which does the
# same thing using a list comprehension. Leave the provided
# implementations as-is and add your code to the functions which end in
# 'LC'.


def addToEach(listOfNumbers, toAdd):
    """
    Adds the given single number to each of the numbers in the provided
    sequence, returning a new list (and not modifying the original list).
    """
    result = []
    for n in listOfNumbers:
        result.append(n + toAdd)

    return result


def addToEachLC(listOfNumbers, toAdd):
    """
    Does the same thing as `addToEach` using a list comprehension.
    """
    result = [n + toAdd for n in listOfNumbers]
    return result


def listFirstNames(namePartsList):
    """
    Given a list containing tuples of strings which include the different
    parts of people's names, returns a list of strings where each entry
    is just that person's first name.
    """
    result = []
    for parts in namePartsList:
        result.append(parts[0])

    return result


def listFirstNamesLC(namePartsList):
    """
    Given a list containing tuples of strings which include the different
    parts of people's names, returns a list of strings where each entry
    is just that person's first name.
    """
    result = [parts[0] for parts in namePartsList]
    return result

def bigNumbers(numsList):
    """
    Given a list of numbers, returns a list containing each number in the
    original list that's larger than 50.
    """
    result = []
    for num in numsList:
        if num > 50:
            result.append(num)

    return result


def bigNumbersLC(numsList):
    """
    Works like `bigNumbers` but using a list comprehension.
    """
    result = [num for num in numsList if num > 50]
    return result


def longWords(wordsList):
    """
    Given a list of words, returns a list containing each word that's
    more than 7 letters long.
    """
    result = []
    for word in wordsList:
        if len(word) > 7:
            result.append(word)

    return result


def longWordsLC(wordsList):
    """
    Works like `longWords` but using a list comprehension.
    """
    result = [word for word in wordsList if len(word) > 7]
    return result

def wordsStartingWith(wordsList, prefix):
    """
    Given a list of words and a prefix string, returns a new list
    containing all of the words from the original list that start with
    the specified prefix.
    """
    result = []
    for word in wordsList:
        if word.startswith(prefix):
            result.append(word)

    return result


def wordsStartingWithLC(wordsList, prefix):
    """
    Works like `wordsStartingWith` but using a list comprehension.
    """
    result = [word for word in wordsList if word.startswith(prefix)]
    return result


def oddSquares(numsList):
    """
    Given a list of numbers, returns a new list containing the square of
    each odd number from the original list.
    """
    result = []
    for num in numsList:
        if num % 2 == 1:
            result.append(num * num)

    return result


def oddSquaresLC(numsList):
    """
    Works like `oddSquares` but using list comprehensions.
    """
    result = [num**2 for num in numsList if num % 2 == 1]
    return result


def fileExtensions(fileNamesList):
    """
    Given a list of file names, returns a new list containing the file
    extension (last 3 letters) of each filename in the list that's at
    least 5 letters long and has a period in it at the 4th-from-last
    position (we assume file extensions are 3 letters long).
    """
    result = []
    for fileName in fileNamesList:
        if len(fileName) >= 5 and fileName[-4] == '.':
            result.append(fileName[-3:])

    return result


def fileExtensionsLC(fileNamesList):
    """
    Works like `fileExtensions` but using list comprehensions.
    """
    result = [fileName[-3:] for fileName in fileNamesList if len(fileName) >= 5 and fileName[-4] == '.']
    return result


def everyOther(items):
    """
    Given a sequence of items, returns a new list containing every other
    item from the original sequence, starting with the first item.
    TODO: This is in a notebook!
    """
    result = []
    for i in range(len(items)):
        if i % 2 == 0:
            result.append(items[i])

    return result


def everyOtherLC(items):
    """
    Works like `everyOther` but using list comprehensions.
    """
    result = [items[i] for i in range(len(items)) if i % 2 == 0]
    return result


def filesWithExtension(directory, extension):
    """
    Returns a list of the full path to each filename in the given
    directory whose name ends with a period followed by the specified
    extension.

    The list is sorted alphabetically using the `sorted` function.
    """
    result = []
    for filename in os.listdir(directory):
        if filename.endswith('.' + extension):
            result.append(os.path.join(directory, filename))

    return sorted(result)


def filesWithExtensionLC(directory, extension):
    """
    Works like `filesWithExtension` but using list comprehensions.
    """
    result = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith('.' + extension)]
    return sorted(result)
