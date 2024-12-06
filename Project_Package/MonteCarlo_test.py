import unittest
import numpy as np
import pandas as pd

from MonteCarlo import Die, Game, Analyzer


class TestDie(unittest.TestCase):
    def setUp(self):
        self.die = Die(np.array([1, 2, 3, 4, 5, 6]))

    def test_init(self):
        with self.assertRaises(TypeError):
            Die([1, 2, 3, 4, 5, 6])
        with self.assertRaises(ValueError):
            Die(np.array([1, 2, 2, 4, 5, 6]))

    def test_change_weight(self):
        self.die.change_weight(1, 2.0)
        self.assertEqual(self.die.show().loc[self.die.show()[
                         'Face'] == 1, 'Weight'].values[0], 2.0)
        with self.assertRaises(IndexError):
            self.die.change_weight(7, 1.0)
        with self.assertRaises(TypeError):
            self.die.change_weight(1, 'not_a_number')

    def test_roll(self):
        rolls = self.die.roll(10)
        self.assertEqual(len(rolls), 10)
        for roll in rolls:
            self.assertIn(roll, [1, 2, 3, 4, 5, 6])

    def test_show(self):
        df = self.die.show()
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertTrue('Face' in df.columns)
        self.assertTrue('Weight' in df.columns)


class TestGame(unittest.TestCase):
    def setUp(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die2 = Die(np.array([1, 2, 3, 4, 5, 6]))
        self.game = Game([die1, die2])

    def test_play(self):
        self.game.play(10)
        self.assertEqual(len(self.game.show()), 10)

    def test_show(self):
        self.game.play(10)
        df_wide = self.game.show('wide')
        df_narrow = self.game.show('narrow')
        self.assertTrue(isinstance(df_wide, pd.DataFrame))
        self.assertTrue(isinstance(df_narrow, pd.DataFrame))
        with self.assertRaises(ValueError):
            self.game.show('invalid_form')


class TestAnalyzer(unittest.TestCase):
    def setUp(self):
        die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
        die2 = Die(np.array([1, 2, 3, 4, 5, 6]))
        game = Game([die1, die2])
        game.play(10)
        self.analyzer = Analyzer(game)

    def test_jackpot(self):
        jackpots = self.analyzer.jackpot()
        self.assertTrue(isinstance(jackpots, int))

    def test_face_counts_per_roll(self):
        face_counts = self.analyzer.face_counts_per_roll()
        self.assertTrue(isinstance(face_counts, pd.DataFrame))

    def test_combo_count(self):
        combos = self.analyzer.combo_count()
        self.assertTrue(isinstance(combos, pd.Series))
