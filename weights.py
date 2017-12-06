"""
These are network weights used in feedforward.py.
"""

from feedforward.py import letters, letterToList, listToLetters
from random import random

def genAbcdWeights():
  # Most of the weights are zero.
  abcdWeights = [ [0 for _ in range(len(letters)) ] for _ in range(len(letters)) ]

  weight = 0.5493 # This is the inverse tanh of 0.5
  abcdWeights[0][3] = weight
  abcdWeights[1][0] = weight
  abcdWeights[2][1] = weight
  abcdWeights[3][2] = weight

abcdWeights = genAbcdWeights()
