"""
These functions -- some pre-written, some fill-in-the-blanks -- should be almost all you need to write a simple neural network.
It won't learn, though.  That's the next section.

Functions you will write are in snake_case.  Given helper functions are in camelCase.

A few useful tips:
  * print() everything that you're not sure about.
  * Make sure each function passes its tests before using it.
  * Use "python -i script-name.py" to run the script, and then put you at a Python command line after it's done.  This 
      way, you can look at all of the variables you set and call the functions you wrote.

"""

from math import exp, log # These are e^x and ln(x), respectively

def tanh(x):
  pass


class Neuron:
  
  # Creating a neuron takes two pieces of information: which other neurons this one gets its input from, and the weight
  #   for each of those connections.  So, we pass them into __init__.  If the neuron is an input neuron, its inputs and
  #   weights should both be set to None.
  def __init__(self, inputs, weights):
    self.inputs = inputs #A list of neurons that this one takes its inputs from
    self.weights = weights #A list of weights. weight[i] corresponds to input[i].

    self.activation = 0 #This should get reset in evaluate()

  def evaluate(self):
    if self.inputs is None:
      return #If this is an input neuron, don't update it.  It doesn't have anywhere to pull its input from!
    else:
      pass #You do the rest!


# This is the five-neuron network from Problems 2 and 4.  It should return the output neuron's activation.
def simple_network():
  pass


# Helper functions for working with letters

letters = "abcdefghijklmnopqrstuvwxyz _"

# Takes a single letter, outputs a list of 28 0's and 1's.
def letterToList(x):
  index = letters.index(x)
  return np.array([0]*index + [0.5] + [0]*(len(letters)-index-1))

# The other way: returns all of the letters, sorted by likelihood, given a list of 28 numbers.
def listToLetters(xs):
  tuples = [ i for i in list(zip(xs,letters)) ]
  tuples = sorted(tuples, key=lambda x: (-x[0],x[1])) #Sort reverse by first value, forward by second
  return [x[1] for x in tuples] #Return just the letters


# These weights are a list of lists.  Sub-list number N contains the weight of every connection leading into output 
#   neuron N, and withing that sub-list, weight number M comes from input neuron M.
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


# This function should take a single character of input, in the form of 28 numbers, and should output the next
#   character in the series "abcdabcd...".  You don't have to worry about any other input.
def abcd_network(inputs):
  pass


# This is the derivative of tanh(x) with regard to x
def tanh_deriv(x):
  pass


# outputDerivs contains the derivative of the whole network's error, with regard to this neuron's output.  This function
#   should both adjust this neuron's weight, and either save or return the values which we'll need to continue backpropagating
#   back from this neuron.
# Note that there *is no test* for this function, because there are a few design choices you get to make.  To see if it works,
#   use the training function below.
def backprop(self, outputDeriv, learnRate):
  pass

# Adds the method to the class
Neuron.backprop = backprop
