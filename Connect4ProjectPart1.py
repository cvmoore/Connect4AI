#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:47:26 2020

@author: cartervandemoore
"""

#
# ps9pr1.py (Problem Set 9, Problem 1)
#
# A Connect Four Board class
#
# Computer Science 111
#

class Board:
    """ a data type for a Connect Four board with arbitrary dimensions
    """   
    #the contructor for the class Board
    def __init__(self, height, width):
        self.height=height
        self.width=width
        self.slots = [[' '] * self.width for row in range(self.height)]
        
        
    def __repr__(self):
        """ Returns a string representation of a Board object.
        """
        s = ''         # begin with an empty string

        # add one row of slots at a time to s
        for row in range(self.height):
            s += '|'   # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'  # newline at the end of the row

        ### add your code here ###
        s+='-'*self.width*2+'-'
        s+='\n'
        for x in range(self.width):
            if x<10:
                s+=' '+str(x)
            else:
                s+=' '+str(x%10)
        return s

    def add_checker(self, checker, col):
        """ adds the specified checker (either 'X' or 'O') to the
            column with the specified index col in the called Board.
            inputs: checker is either 'X' or 'O'
                    col is a valid column index
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)
        
        ### put the rest of the method here ###
        n=0
        lst=[x for x in range(self.height)]
        lst1=lst[::-1]
        for x in lst1:
            if self.slots[x][col]!='X' and self.slots[x][col]!='O':
                n=x
                break
        self.slots[n][col]=checker
    
    ### add your reset method here ###
    
    def add_checkers(self, colnums):
        """ takes a string of column numbers and places alternating
            checkers in those columns of the called Board object,
            starting with 'X'.
            input: colnums is a string of valid column numbers
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    ### add your remaining methods here
    #returns a board that is reset by being all ' '
    def reset(self):
        self.__init__(self.height, self.width)
    
    #returns True if the the player has entered a valid column
    def can_add_to(self, col):
        lst=[x for x in range(self.width)]
        if(col in lst and self.slots[self.height-1][col]==' '):
            return True
        else: 
            return False
    
    #checks if board is entirely full
    def is_full(self):
        for c in range(self.width):
            if self.can_add_to(c)!=False:
                return False
                break
        return True
    
    #Removes the top checker from a specific column
    def remove_checker(self, col):
        for r in range(self.height):
            if(self.slots[r][col]=='X' or self.slots[r][col]=='O'):
                self.slots[r][col]=' '
                break
            elif(r==self.height-1 and self.slots[r][col]==' '):
                break
        
    #checks for horizontal win
    def is_horizontal_win(self, checker):
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                    self.slots[row][col + 1] == checker and \
                    self.slots[row][col + 2] == checker and \
                    self.slots[row][col + 3] == checker:
                        return True
        return False    
    
    #checks for vertical win
    def is_vertical_win(self, checker):
        for row in range(self.height-3):
            for col in range(self.width):
                if self.slots[row][col] == checker and \
                    self.slots[row+1][col] == checker and \
                    self.slots[row+2][col] == checker and \
                    self.slots[row+3][col] == checker:
                        return True
        return False 
     
    #checks for down diagonal win
    def is_down_diagonal_win(self, checker):
        for row in range(self.height-3):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                    self.slots[row+1][col+1] == checker and \
                    self.slots[row+2][col+2] == checker and \
                    self.slots[row+3][col+3] == checker:
                        return True
        return False 

    #checks for down diagonal win
    def is_up_diagonal_win(self, checker):
        for row in range(3,self.height):
            for col in range(self.width-3):
                if self.slots[row][col] == checker and \
                    self.slots[row-1][col+1] == checker and \
                    self.slots[row-2][col+2] == checker and \
                    self.slots[row-3][col+3] == checker:
                        return True
        return False 
    
    #checks if there are 4 consecutive of the same type
    def is_win_for(self, checker):
        assert(checker == 'X' or checker == 'O')
        if self.is_up_diagonal_win(checker)==True or \
            self.is_down_diagonal_win(checker)==True or \
            self.is_vertical_win(checker)==True or \
            self.is_horizontal_win(checker)==True:
                return True
        else: 
            return False