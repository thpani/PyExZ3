from z3 import *

from adder import addN

def multN(xN, yN):
  res = []
  cout = BoolVal(False)
  new_res = [ And(yN[0], xi) for xi in xN ]
  res.append(new_res[0])
  for yi in yN[1:]:
    adder_input_1 = [ And(yi, xi) for xi in xN ]
    adder_input_2 = new_res[1:] + [ cout ]
    new_res, cout = addN(adder_input_1, adder_input_2, BoolVal(False))
    res.append(new_res[0])
  return res
