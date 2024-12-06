import numpy as np
import pandas as pd


class Die:
    """
    This class creates a Die, allows the user to change the weights of the die, '.change_weight'
    allows the user to roll a specified amount of times with '.roll' (Default n of rolls is 1).
    Initiates with the number of faces the user wants the die to have
    """

    def __init__(self, faces):
        if not isinstance(faces, np.ndarray):
            raise TypeError("Faces must be a NumPy array")
        if len(np.unique(faces)) != len(faces):
            raise ValueError("Faces must be unique")
        self._faces = faces
        self._weights = np.ones(len(faces))
        self._df = pd.DataFrame({'Face': faces, 'Weight': self._weights})

    def change_weight(self, face, weight):
        """Inputs are face and weight. Changes the weight of the die on the specified face. 
        Does not allow to change the weight of a face that does not exist."""
        if face not in self._df['Face'].values:
            raise IndexError("Face value not in die faces")
        if not isinstance(weight, (int, float)):
            raise TypeError("Weight must be numeric")
        self._df.loc[self._df['Face'] == face, 'Weight'] = weight

    def roll(self, rolls=1):
        """
        Rolls the die a specified number of times. If number of rolls isnt specified, it will roll once.
        """
        return self._df.sample(n=rolls, replace=True, weights='Weight')['Face'].tolist()

    def show(self):
        """
        shows the results of the roll(s)
        """
        return self._df.copy()
