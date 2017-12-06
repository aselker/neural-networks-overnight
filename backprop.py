"""
You've learned to evaluate a neural network.  Now you'll train them!
As before, camelCase is prewritten, snake_case needs your help.
"""

# This pulls in everything from the last .py file.
from feedforward import *

# This is the derivative of tanh(x) with regard to x
def tanh_deriv(x):
  pass


class Neuron:
  
  # Creating a neuron takes two pieces of information: which other neurons this one gets its input from, and the weight
  #   for each of those connections.  So, we pass them into __init__.  If the neuron is an input neuron, its inputs and
  #   weights should both be set to None.
  def __init__(self, inputs, weights):
    self.inputs = inputs #A list of neurons that this one takes its inputs from
    self.weights = weights #A list of weights. weight[i] corresponds to input[i].

    self.activation = 0 #This should get reset in evaluate()

  # You can copy this implementation over from feedforward.py.  However, you might want to save the result of the evaluation
  #   in a local variable, for use in the backprop function.
  def evaluate(self):
    pass

  # outputDerivs contains the derivative of the whole network's error, with regard to this neuron's output.  This function
  #   should both adjust this neuron's weight, and either save or return the values which we'll need to continue backpropagating
  #   back from this neuron.
  # Note that there *is no test* for this function, because there are a few design choices you get to make.  To see if it works,
  #   use the training function below.
  def backprop(self, outputDeriv, learnRate):

