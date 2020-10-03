#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:49:46 2020

@author: cartervandemoore
"""

#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Playing the game 
#   
 
from Connect4ProjectPart1 import Board
from Connect4ProjectPart2 import Player
import random
    
def connect_four(p1, p2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: p1 and p2 are objects representing Connect Four
          players (objects of the Player class or a subclass of Player).
          One player should use 'X' checkers and the other should
          use 'O' checkers.
    """
    # Make sure one player is 'X' and one player is 'O'.
    if p1.checker not in 'XO' or p2.checker not in 'XO' \
       or p1.checker == p2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    b = Board(6, 7)
    print(b)
    
    while True:
        if process_move(p1, b) == True:
            return b

        if process_move(p2, b) == True:
            return b

#performs all of the steps involved in processing a single move by player p 
#on board b
def process_move(p, b):
    print(p.__repr__()+"'s turn")
    p_col=p.next_move(b)
    b.add_checker(p.checker, p_col)
    print()
    print(b)
    if(b.is_win_for(p.checker)==True):
        print(p.__repr__()+" wins in "+str(p.num_moves)+" moves")
        print('Congratulations!')
        return True
    elif(b.is_full()==True):
        print("It's a tie!")
        return True
    else:
        return False

#used for an unintelligent computer player that chooses at random 
#from the available columns
class RandomPlayer(Player):
    def next_move(self, board):
        self.num_moves+=1
        lst=[x for x in range(board.width) if board.can_add_to(x)==True]
        ans=random.choice(lst)
        return int(ans)
        