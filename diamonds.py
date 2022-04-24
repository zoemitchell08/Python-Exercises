"""
Authors: Zoe Mitchell
Consulted:
Date: 05-02-22
Purpose: Diamonds task: draw a diamond pattern using functions and a
limited number of print function calls.
"""

#---------------------#
# Pre-defined strings #
#---------------------#

# You're not allowed to create any other new strings with quotes in this
# program, except for the docstrings for each of your functions!

zero  = '     '
one   = '  1  '
two   = ' 2 2 '
three = '3 3 3'
empty = ''

def oneRow():
    """this prints the first row of four diamonds with no indentation"""
    print((one + zero)*4)
    print((two + zero)*4)
    print((three + zero)*4)
    print((two + zero)*4)
    print((one + zero)*4)
    
def indentRow():
    """this prints a row below oneRow of another four diamons with indentation"""
    print((zero + one)*4)
    print((zero + two)*4)
    print((zero + three)*4)
    print((zero + two)*4)
    print((zero + one)*4)
    

def diamondPattern():
    """each function that prints out a row of diamonds is called to make the diamond pattern"""
    oneRow()
    indentRow()
    oneRow()
    indentRow()
    oneRow()
    indentRow()
    oneRow()
    indentRow()
 

# Define diamondPattern and other necessary helper functions --> diamondPattern has to call another functions(s) at least twice!!
# Be sure to use meaningful function names, parameter names, and
# variable names.
#do not use print within diamondPattern (only outside or in helper functions)

# Comment your code appropriately
# In particular, every function definition must have a
# triple-quoted docstring between the header and the body
# that briefly explains what the function does.
