# Name: Sean Plisner
# QCC ID: 24363905
# ET574 Homework 4 - Dice Game Simulator

import random

class Die: 
    def__init__(self, max_side=6):
        self.max_side = max_side
    def roll(self):
        return.randint(1, self.max_side)