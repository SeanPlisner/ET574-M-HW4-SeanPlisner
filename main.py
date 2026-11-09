# Name: Sean Plisner
# QCC ID: 24363905
# ET574 Homework 4 - Dice Game Simulator

import random

class Die: 
    def__init__(self, max_side=6):
        self.max_side = max_side
    def roll(self):
        return.randint(1, self.max_side)

class DiceGame: 
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()

    def evalulate_roll(self, total):
        if total == 7 or total == 11:
            return "win"
        elif total == 2 or total == 3 or total == 12:
            return "lose"
        else:
            return "Roll Again" 

    def play_round(self):
        roll1 = self.die1.roll()
        roll2 = self.die2.roll()

        total = roll1 + roll2

        result = self.evalulate_roll(total)

        return roll1, roll2, total, result 
    
def main():
    game = DiceGame()

    while true:
        print("\nDice Game simulator")
        print("1. Play a round")
        print("2. Exit")

        choice = input("Enter your choice.")

        if choice == 1:
            die1, die2, total, result = game.play_round

            print("\nYou rolled", die1, "and", die2)
            print("Total:", total)
            print("Result:", result)

        elif choice == 2:
            print("Thanks for playing!")
            break 
        
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
