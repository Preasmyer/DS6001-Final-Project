import numpy as np
import pandas as pd


class Game:
    """
    This class consists of rolling one or more dice multiple times.
    """

    def __init__(self, dice):
        """
        an intialization method that takes a list of Die objects
        """
        self._dice = dice
        self._results = None

    def play(self, rolls):
        """
        A method that rolls the die a specified number of times and Stores the results in a local DataFrame.
        """
        results = []
        for _ in range(rolls):
            roll_results = [die.roll()[0] for die in self._dice]
            results.append(roll_results)
        self._results = pd.DataFrame(results)

    def show(self, form='wide'):
        """
        Shows the results of the play when called.
        """
        if form == 'wide':
            return self._results.copy()
        elif form == 'narrow':
            return self._results.melt(var_name='Die', value_name='Face', ignore_index=False)
        else:
            raise ValueError("Form must be 'wide' or 'narrow'")
