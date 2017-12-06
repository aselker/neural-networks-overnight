"""
These are tests for backprop.py.
"""

from feedforward-tests import *
import backprop as bp

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


