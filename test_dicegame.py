# Name: Sean Plisner
# QCC ID: 24363905
# ET574 Homework 4 - Dice Game Unit Tests

import unittest
from unittest.mock import patch
from main import Die, DiceGame


Class TestDiceGame(unittest.TestCase):

    def test_custom_die_roll_bounds(self):
        die = Die(10)

        for i in range(100)
            roll = die.roll()
            self.assertGreaterEqual(roll, 1)
            self.assertLessEqual(roll, 10)

    def test_evaluate_roll_11_is_win(self):
        game = DiceGame()
        result = game.evaluate_roll(11)

        self.assertEqual(result, "Win")

    def test_evaluate_roll_12_is_lose(self):
         game = DiceGame()
         result = game.evaluate_roll(12)

         self.assertEqual(result, "Lose")

    def test_play_round_total_matches_dice(self):
        game = DiceGame()

        with patch.object(game.die1, "roll", return_value=3):
            with patch.object(game.die2, "roll", return_value=4):
                die1, die2, total, result = game.play_round()
        
        self.assertEqual(die1, 3)
        self.assertEqual(die2, 4)
        self.assertEqual(total, 7)
        self.assertEqual(result, "Win")

if __name__ == "__main__":
    unittest.main()