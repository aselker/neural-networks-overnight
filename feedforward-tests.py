"""
These are reference implementations and tests for feedforward.py.
Please try to solve the problems before looking here!


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


def simpleNetwork_test():
  return (ff.simpleNetwork() is not None) and (abs(fiveNeuronReferenceOutput - ff.simpleNetwork()) < epsilon)

if simpleNetwork_test():
  print("Simple network pass")
else:
  print("Simple network fail")
