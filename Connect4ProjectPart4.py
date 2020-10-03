#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 14:50:02 2020

@author: cartervandemoore
"""

#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from Connect4ProjectPart3 import *


class AIPlayer(Player):
    
    #Constructs a new AIPlayer Object
    def __init__(self, checker, tiebreak, lookahead):
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak=tiebreak
        self.lookahead=lookahead
        
    def __repr__(self):
        ans="Player "+str(self.checker)+" ("+str(self.tiebreak)+", "+str(self.lookahead)+")"
        return ans
    
    #returns the index of the column with the maximum score or
    #uses its tiebreak strategy to determine a column
    def max_score_column(self, scores):
        max_score=max(scores)
        lst_ans=[x for x in range(len(scores)) if scores[x]==max_score]
        if(lst_ans==1):
            return lst_ans[0]
        else:
            if(self.tiebreak=="LEFT"):
                return lst_ans[0]
            elif(self.tiebreak=="RIGHT"):
                return lst_ans[len(lst_ans)-1]
            else:
                return random.choice(lst_ans)
    
    #determines the called AIPlayer's scores for the columns in b    
    def scores_for(self, b):
        scores=[50]*b.width
        for col in range(b.width):
            if(b.can_add_to(col)==False):
                scores[col]=-1
            elif(b.is_win_for(self.checker)):
                scores[col]=100
            elif(b.is_win_for(self.opponent_checker())):
                scores[col]=0
            elif(self.lookahead==0):
                scores[col]=50
            else:
                b.add_checker(self.checker, col)
                opponent=AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead-1)
                opp_scores=opponent.scores_for(b)
                if(max(opp_scores)==100):
                    scores[col]=0
                elif(max(opp_scores)==50):
                    scores[col]=50
                elif(max(opp_scores)==0):
                    scores[col]=100
                else:
                    scores[col]=-1
                b.remove_checker(col)
        return scores
    
    #return the called AIPlayer's judgment of its best possible move
    def next_move(self, b):
        ans=self.max_score_column(self.scores_for(b))
        return ans
        