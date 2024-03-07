
from fractions import Fraction
 
def fractionate(amount: int):
    # numerator, denominator
    fraction = Fraction(1, amount)
 
    return [fraction] * amount
