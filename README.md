# DS6001-Final-Project
The Final Project for DS 6001 - Programming for Data Science

# MonteCarloSimulator

## Metadata

- **Name:** MonteCarloSimulator
- **Version:** 1.0.0
- **Author:** Cameron Preasmyer
- **Email:** spc6uz@virginia.edu
- **Description:** A Monte Carlo simulator with Die, Game, and Analyzer classes.
- **License:** MIT License
- **Repository URL:** [https://github.com/Preasmyer/DS6001-Final-Project](https://github.com/Preasmyer/DS6001-Final-Project)

## Synopsis

### Die Class

The `Die` class represents a die with a specified number of faces and weights. It allows you to roll the die and change the weight of specific faces.

Below are some examples of how to use the Die class

```python
from MonteCarlo import Die
import numpy as np

# Example of how to create a die with faces 1 through 6
die = Die(np.array([1, 2, 3, 4, 5, 6]))

# Example on how to change the weight of face 1 to 2.0
die.change_weight(1, 2.0)

# Example of how to roll the die 10 times (replace 10 with any number for n rolls)
results = die.roll(10)

# Example of how to show the current state of the die created
die.show()
```

### Game Class 

The `Game` class consists of rolling one or more dice multiple times and stores the results. 
Below are some example of how the 'Game' class works and how to use it.
```python

from MonteCarlo import Game 
# Example of creating a game with two dice 
die1 = Die(np.array([1, 2, 3, 4, 5, 6]))
die2 = Die(np.array)[1, 2, 3, 4, 5, 6]))
game = Game([die1, die2])
```
The 'Analyzer' class takes the results of a game and computes various descriptive statistical properties.

Below are some examples of how to use this class.

```python
from MonteCarlo import Analyzer

# How to create an Analyzer. The Analyzer takes the game object as an input.
analyzer = Analyzer(game)

# Example of how to compute the number of jackpots in your rolls
jackpots = analyzer.jackpot()

# Example of how to compute the face counts per roll
face_counts = analyzer.face_counts_per_roll()

# Example of how to compute the distinct combinations of faces rolled
combos = analyzer.combo_count()

# Example of how to compute the distinct permutations of faces rolled
permutations = analyzer.permutation_count()
```

#API

##Die Class

__init__(self, faces): Initialize the die with faces and default weights.

#### Parameters:

faces (numpy.ndarray): Array of faces for the die.

#### Raises:

TypeError: If faces is not a NumPy array.

ValueError: If faces are not unique.

change_weight(self, face, weight): Change the weight of a specific face.

#### Parameters:

face: The face value whose weight is to be changed.

weight (float): The new weight for the face.

#### Raises:

IndexError: If face value is not in die faces.

TypeError: If weight is not a numeric value.

roll(self, rolls=1): Roll the die a specified number of times.

#### Parameters:

rolls (int): Number of times to roll the die. Defaults to 1.

#### Returns:

list: List of outcomes from the rolls.

show(self): Show the current state of the die.

#### Returns:

pandas.DataFrame: DataFrame representing the die's faces and weights.

# Game Class
__init__(self, dice): Initialize the game with a list of dice.

#### Parameters:

dice (list): List of Die objects.

play(self, rolls): Roll all dice a specified number of times.

#### Parameters:

rolls (int): Number of times to roll the dice.

show(self, form='wide'): Show the results of the most recent play.

#### Parameters:

form (str): Format of the results ('wide' or 'narrow'). Defaults to 'wide'.

#### Raises:

ValueError: If an invalid format is specified.

# Analyzer Class
__init__(self, game): Initialize the analyzer with a game object.

#### Parameters:

game (Game): A Game object.

#### Raises:

ValueError: If the input is not a Game object.

jackpot(self): Compute the number of jackpots in the game.

#### Returns:

int: Number of jackpots.

face_counts_per_roll(self): Compute the face counts for each roll.

#### Returns:

pandas.DataFrame: DataFrame of face counts per roll.

combo_count(self): Compute the distinct combinations of faces rolled.

#### Returns:

pandas.Series: Series of distinct combinations and their counts.

permutation_count(self): Compute the distinct permutations of faces rolled.

#### Returns:

pandas.Series: Series of distinct permutations and their counts.
