"""
These are reference implementations and tests for feedforward.py.
Please try to solve the problems before looking here!


"""

from math import exp, log
import feedforward as ff


def tanh(x):
  return ( exp(x) - exp(-x) ) / ( exp(x) + exp(-x) )

def tanh_test():
  # Because we are working with floating-point numbers, different, valid ways of computing the same thing can give slightly different
  #   answers.  So, we need a definition of equality that has some slop.  We use this epsilon as the smallest allowable difference.
  epsilon = 0.0001

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


