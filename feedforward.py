"""
These functions -- some pre-written, some fill-in-the-blanks -- should be almost all you need to write a simple neural network.
It won't learn, though.  That's the next section.

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
def simpleNetwork():
  pass


# Helper functions for working with letters

letters = "abcdefghijklmnopqrstuvwxyz _"

def letterToList(x):
  index = letters.index(x)
  return np.array([lowState]*index + [highState] + [lowState]*(len(letters)-index-1))

def listToLetters(xs):
  tuples = [ i for i in list(zip(xs,letters)) ]
  tuples = sorted(tuples, key=lambda x: (-x[0],x[1])) #Sort reverse by first value, forward by second
  return [x[1] for x in tuples] #Return just the letters

def printLetterWeights(xs, removeZeros = False):
  tuples = [i for i in list(zip(xs,letters)) if (i[0] > 0.01 or not removeZeros)] #Remove the ~zeroes
  tuples = sorted(tuples, key=lambda x: (-x[0],x[1])) #Sort reverse by first value, forward by second
  for i in tuples:
    if len(str(i[0])) > 5:
      print(str(i[0])[0:6] + ":\t" + str(i[1])) #Limit digits
    else:
      print(str(i[0]) + ":\t" + str(i[1])) #All the digits

