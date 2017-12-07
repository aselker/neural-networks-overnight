"""
These are tests for feedforward.py.
They probably aren't very helpful for solving the problems.  If you want help, ask a Ninja!
However, feel free to modify these, such as if you'd like to change how a function's arguments are arranged.
"""

from math import exp, log
import feedforward as ff


def tanh(x):
  return ( exp(x) - exp(-x) ) / ( exp(x) + exp(-x) )

# Because we are working with floating-point numbers, different, valid ways of computing the same thing can give slightly different
#   answers.  So, we need a definition of equality that has some slop.  We use this epsilon as the smallest allowable difference.
epsilon = 0.0001

def tanh_test():
  for i in [-1, 0, 1, 2]: # Try four cases
    # If the function hasn't been implemented yet, or if the implementations differ, return false.
    if (ff.tanh(i) is None) or (abs(tanh(i) - ff.tanh(i)) > epsilon):
      return False

  # Otherwise return true.
  return True

if tanh_test():
  print("tanh pass")
else:
  print("tanh fail")


fiveNeuronReferenceOutput = tanh( tanh(0.5*1 + 1*0.5) * 2 + tanh(0.5*0.5 + 1*2) * 1 )

def neuron_test():
  input_1 = ff.Neuron(None, None)
  input_2 = ff.Neuron(None, None)
  hidden_1 = ff.Neuron([input_1, input_2], [1, 0.5])
  hidden_2 = ff.Neuron([input_1, input_2], [0.5, 2])
  output_1 = ff.Neuron([hidden_1, hidden_2], [2, 1])

  input_1.activation = 0.5
  input_2.activation = 1
  hidden_1.evaluate()
  hidden_2.evaluate()
  output_1.evaluate()

  if abs(fiveNeuronReferenceOutput - output_1.activation) > epsilon:
    return False
  else:
    return True

if neuron_test():
  print("Neuron class pass")
else:
  print("Neuron class fail")


def simple_network_test():
  return (ff.simple_network() is not None) and (abs(fiveNeuronReferenceOutput - ff.simple_network()) < epsilon)

if simple_network_test():
  print("Simple network pass")
else:
  print("Simple network fail")


def abcd_network_test():

  # To test the network, we check whether the first output is what we expect.
  if listToLetters(abcd_network(letterToList("a")))[0] != b:
    return False 
  if listToLetters(abcd_network(letterToList("b")))[0] != c:
    return False
  if listToLetters(abcd_network(letterToList("c")))[0] != d:
    return False
  if listToLetters(abcd_network(letterToList("d")))[0] != a:
    return False

  return True

if abcd_network_test():
  print("abcd network pass")
else:
  print("abcd network fail")


def tanh_deriv(x):
  return 1 - (tanh(x)**2)


def tanh_deriv_test():
  for i in [-1, 0, 1, 2]: # Try four cases
    # If the function hasn't been implemented yet, or if the implementations differ, return false.
    if (bp.tanh_deriv(i) is None) or (abs(tanh_deriv(i) - bp.tanh_deriv(i)) > epsilon):
      return False

  # Otherwise return true.
  return True

if tanh_deriv_test():
  print("tanh_deriv pass")
else:
  print("tanh_deriv fail")

