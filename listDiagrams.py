"""
Authors: Zoe Mitchell
Consulted:
Date: 03/04/22
Purpose: listDiagrams task:
         create lists with specified list diagram structures
"""


#-------------------------------------------------------------------------#
# SAMPLE FUNCTIONS FROM THE listDiagrams PROBLEM DESCRIPTION              #
#-------------------------------------------------------------------------#

def makeList0_approach1():
    '''
    Returns the top list depicted in the memory diagram for list0.
    Uses Approach 1 to create the appropriate list structure.
    '''
    shared2 = [2]
    shared1 = [1, shared2]
    top = [shared1, shared2, shared1, shared2]
    return top


def makeList0_approach2():
    '''
    Returns the top list depicted in the memory diagram for list0.
    Uses Approach 2 to create the appropriate list structure.
    '''
    top = [3, 4, 5, [2]]
    top[0] = [1, top[3]]
    top[1] = top[3]
    top[2] = top[0]
    return top


def makeList0_approach3():
    '''
    Returns the top list depicted in the memory diagram for list0.
    Uses Approach 3 to create the appropriate list structure.
    '''
    top = [[1]]
    top[0].append([2])
    top.append(top[0][1])
    top.append(top[0])
    top.append(top[1])
    return top


#-------------------------------------------------------------------------#
# FUNCTIONS TO COMPLETE                                                   #
#                                                                         #
# Each of the following functions should return a list structure for      #
# the top list in the corresponding memory diagrams in the problem set    #
# specifiction. To specify sharing/aliasing, you may introduce local      #
# variables that do not appear in the diagrams.                           #
#-------------------------------------------------------------------------#

def makeList1():
    '''
    Returns the top list depicted in the memory diagram for list1.
    '''
    share1 = [1, 2]
    share2 = [1, 2]
    top = [share1, 3, share2]
    return top


def makeList2():
    '''
    Returns the top list depicted in the memory diagram for list2.
    '''
    shared = [1, 2]
    top = [shared, 3, shared]
    return top


def makeList3():
    '''
    Returns the top list depicted in the memory diagram for list3.
    '''
    shared3 = [3]
    shared2 = [shared3, 2]
    shared1 = [1, shared2]
    top = [shared1, shared2, shared3]
    return top
    


def makeList4():
    '''
    Returns the top list depicted in the memory diagram for list4.
    '''
    top = [0, 1, 2, 3]
    shared1 = [4, 5]
    shared2 = [4, 5]
    top[0] = shared1
    top[2] = [shared1, shared2]
    top[1] = [shared1, top[2]]
    top[3] = shared2
    
    
    return top
    


def makeList5():
    '''
    Returns the top list depicted in the memory diagram for list5.
    ''' 
    top = ['parent', 1]
    shared1 = ['child1', top]
    shared2 = ['child2', top]
    top[1] = [shared1, shared2]
    return top


def makeList6():
    '''
    Returns the top list depicted in the memory diagram for list6.
    '''
    shared1 = [0, 6, 2]
    shared2 = [7, shared1, 8, 3]
    shared2[3] = shared2
    shared1[0] = shared2
    shared1[2] = shared2
    
    return shared1