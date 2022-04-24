"""
Authors:
Consulted:
Date:
Purpose: wordSearch task: finds words hidden in a grid of letters.
"""
import wordPuzzle


#-----------#
# Your code #
#-----------#

def printGrid(rows):
    """
    Given a list of letter rows (each of which is a string of the same length)
    displays a two-dimensional grid which (1) there is a space after each
    letter and (2) there is a blank line after each row.

    Recall that the newline character '\n` causes a printed string to move to
    the next line. Calls to `print` normally end with a newline, but this can
    be overridden by the keyword argument `end`. E.g., print('hello`, end=' ')
    will display the five characters in `hello` followed by a space rather than
    a newline.
    """
    for string in rows:
        for letter in string:
            print(letter + ' ', end='')
        print('')
        print('')
        

def getColumns(rows):
    """
    Given a list of row strings representing a text grid, returns a list of
    strings that are the columns in the given rows. In the result, the first
    string should be the characters in the first column of the grid, 
    the second string should be the characters in the second column of the grid, 
    and so on. 

    For example, `getColumns( ["abcd", "efgh", "ijkl" ] )` should
    return the list of column strings `["aei", "bfj", "cgk", dhl"]`.
    """
    transposed = []
    
    for i in range(len(rows[0])):
        newStr = ''
        for string in rows:
            newStr = newStr + string[i]
        transposed.append(newStr)


    return transposed


def getColumns2(rows):
    """
    An alternative implementation of `getColumns` which uses a different
    loop structure. This function does not need to be defined :/
    """
    # Replace this stub
    return []

def findHorizontals(rows, wordlist):
    """
    Assume that `rows` is a list of strings representing the puzzle text grid,
    and `wordlist` is a list words (strings) hidden in the grid.  This function
    finds all the words in `wordlist` that appear in the puzzle with a forward
    horizontal orientation. 

    This function returns a list of **location entries** that indicate
    which words were found horizontally and where. Each location
    entry is a tuple with 4 components: 

    1. The word that was found; 
    2. The string 'H', to indicate the word was found horizontally; 
    3. The row (an integer, starting from 0) where the 
       forward horizontal word starts.
    4. The column (an integer, starting from 0) where the 
       forward horizontal word starts.

    The tuples should be ordered so that the found words have the same relative
    order as the words in `wordList`.

    To find the first index at which a word appears as a substring in a
    row string, use Python's `.find` method on strings, which returns
    this index (or -1 if the word is not found). For example: 

      'concatenate'.find('cat') => 3
      'rationalization'.find('tion') => 2 # index for 1st of 2 matches
      'concatenate'.find('dog') => -1
    """
    found = []
    rowNum = 0
    for line in rows:
        for word in wordlist:
            isIt = line.find(word)
            if isIt != -1:
                foundItem = word, 'H', rowNum, isIt
                found.append(foundItem)
        rowNum += 1
    return found

def findVerticals(rows, wordlist):
    """
    Assume that `rows` is a list of strings representing the puzzle text grid,
    and `wordlist` is a list words (strings) hidden in the grid.  This function
    finds all the words in `wordlist` that appear in the puzzle with a downward
    vertical orientation. 

    This function returns a list of **location entries** that indicate
    which words were found horizontally and where. Each location
    entry is a tuple with 4 components: 

    1. The word that was found.
    2. The string 'V' to indicate a vertical match.
    3. The row (an integer, starting from 0) where the 
       downward vertical word starts.
    4. The column (an integer, starting from 0) where the 
       downward veritcal word starts.

    The tuples should be ordered so that the found words have the
    same relative order as the words in `wordList`. 

    Your `findVerticals` function should *not* loop over `wordList` or `rows`.
    Rather, it should use `findHorizontals` on the result of   `getColumns`,
    and then use a mapping-pattern loop or list comprehension to change the tuples
    returned by `findHorizontals` to be the correct tuples for `findVerticals`.
    """
    finalList = []
    rearranged = getColumns(rows)
    search = list(findHorizontals(rearranged, wordlist))
    for item in search:
        tempList = list(item)
        tempList[1] = 'V'
        firstNum = tempList[2]
        secNum = tempList[3]
        tempList[2] = secNum
        tempList[3] = firstNum
        finalList.append(tuple(i for i in tempList))
      
    return sorted(finalList)

def findWords(rows, wordlist):
    """
    Assume that `rows` is a list of strings representing the puzzle text grid,
    and `wordlist` is a list words (strings) hidden in the grid.  This function
    finds all the words in `wordlist` that appear in the puzzle in either a
    forward horizontal or downward vertical direction.

    It returns a list of location entries, which are 4-tuples that have
    the following parts:

    1. The word found.
    2  The string 'H' if the word is horizontal forward word or 
       'V' if it's a vertical downward word. 
    3. The row (an integer, starting from 0) where the word begins
    4. The column (an integer, starting from 0) where the word begins

    The location entries should be sorted in ascending alphabetical
    order by the word. Use the `sorted` function for this purpose. 

    Note that findWords will *not* find words in the puzzle
    that are horizontally backward, vertically upward, or
    oriented diagonally. 
    """
    horizontal = findHorizontals(rows, wordlist) 
    vertical = findVerticals(rows, wordlist)
    final = (horizontal + vertical)
    
    return sorted(final)

#---------#
# Testing #
#---------#

# Below is one test grid for testing.
# For more extensive testing, run the file test_wordSearch.py

# These variables define a very simple nonrandom puzzle and the words
# embedded in it to help you test things. Because the functions in
# this task search only for words oriented in the forward horizontal
# and vertical downward directions, they will not find these three words:
# 
# * 'cs111' is oriented diagonally
# * 'wellesley' is oriented horizontally, but backwards
# * 'computer' is oriented vertically, but upwards

TEST_PUZZLE = [
    "----s-------",
    "----center--",
    "p---i--r----",
    "yelsellew---",
    "t-o-n--t----",
    "h-o-c--u---1",
    "o-p-e--p--1-",
    "nested-m-1--",
    "-------os---",
    "-------c----"
]

TEST_WORDS = [
    "cs111",
    "science",
    "center",
    "wellesley",
    "python",
    "computer", 
    "nested", 
    "loops"
]

# TEST_MATCHES is the correct result for findWords(TEST_PUZZLE, TEST_WORDS).
TEST_MATCHES = [
    ('center', 'H', 1, 4), 
    ('loops', 'V', 3, 2), 
    ('nested', 'H', 7, 0), 
    ('python', 'V', 2, 0), 
    ('science', 'V', 0, 4)
]

