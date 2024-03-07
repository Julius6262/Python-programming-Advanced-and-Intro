def balanced_brackets(my_string: str):
    brackets = [char for char in my_string if char in '()[]']
    
    if len(brackets) == 0:
        return True
    elif (brackets[0] == '(' and brackets[-1] == ')') or (brackets[0] == '[' and brackets[-1] == ']'):
        return balanced_brackets(brackets[1:-1])
    else:
        return False

def balanced_brackets_2(mj: str):
    # string is empty, so it is ok
    if len(mj) == 0:
        return True
 
    # if first character is not any bracket, let's eat it away
    if not mj[0] in "()[]":
        return balanced_brackets_2(mj[1:])
 
    # if last is not any bracket, let's eat it away
    if not mj[-1] in "()[]":
        return balanced_brackets_2(mj[:-1])
    
    # now is known that first and last characters are brackets
    # check if they are a pair
    if mj[0]=="(" and mj[-1]==")":
        return balanced_brackets_2(mj[1:-1])
    if mj[0]=="[" and mj[-1]=="]":
        return balanced_brackets_2(mj[1:-1])
 
    # were not, so this string is not ok
    return False