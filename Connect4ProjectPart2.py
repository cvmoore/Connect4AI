#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:48:32 2020

@author: cartervandemoore
"""

#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from Connect4ProjectPart1 import Board

# write your class below
class Player():
    
    def __init__(self, checker):
        assert(checker == 'X' or checker == 'O')
        self.checker=checker
        self.num_moves=0
        
    def __repr__(self):
        ans="Player "+str(self.checker)
        return ans

    #Assigns a checker to the opponent
    def opponent_checker(self):
        if(self.checker=='O'):
            return 'X'
        else:
            return 'O'
    
    #get a move from this player that is valid for the board b
    def next_move(self, b):
        self.num_moves+=1
        
        while True:
            col=int(input('Enter a column: '))
            if(b.can_add_to(col)==True):
                return int(col)
                break
            else:
                print('Try Again!')
        