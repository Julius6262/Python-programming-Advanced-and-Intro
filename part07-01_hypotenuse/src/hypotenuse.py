# Write your solution here
import math



def hypotenuse(leg1: float, leg2: float) -> float:
    leng_hypo_raised = leg1**2 + leg2**2
    leng_hypo = math.sqrt(leng_hypo_raised)
    
    return leng_hypo