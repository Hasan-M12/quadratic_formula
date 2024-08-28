def quadratic_formula(valuea, valueb, valuec):
  minus_b = valueb * -1
  denom = 2 * valuea
  bee_squared = valueb * valueb
  four_ac = 4 * valuea * valuec
  subtraction = bee_squared - four_ac
  square_root = (subtraction)**0.5
  sum1 = (minus_b + square_root)/denom
  sum2 = (minus_b - square_root)/denom
  print(sum1, sum2)
