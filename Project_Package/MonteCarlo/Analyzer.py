import numpy as np
import pandas as pd
from .Game import Game


class Analyzer:
    """
    This class takes the results of a game and computes various descriptive statistics
    """

    def __init__(self, game):
        """
        Takes a Game object as an initialization.
        """
        if not isinstance(game, Game):
            raise ValueError("Input must be a Game object")
        self._game = game
        self._results = game.show()

    def jackpot(self):
        """
        Computes how many times all faces from the game are the same.
        """
        return int((self._results.nunique(axis=1) == 1).sum())

    def face_counts_per_roll(self):
        """
        Computes the amount of times that each face is rolled per event.
        """
        return self._results.apply(pd.Series.value_counts, axis=1).fillna(0)

    def combo_count(self):
        """
        Computes distinct combinations of faces rolled in the game.
        """
        combos = self._results.apply(lambda x: tuple(sorted(x)), axis=1)
        return combos.value_counts()

    def permutation_count(self):
        """
        Computes the distinct permutations of faces rolled.
        """
        permutations = self._results.apply(tuple, axis=1)
        return permutations.value_counts()
