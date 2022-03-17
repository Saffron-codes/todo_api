import random
lower = "abcdefghijklmnoqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]{}#()*;._-"

def genNoteId():
    return "".join(random.sample(lower+upper+number+symbol,10))

def genUserId():
    return "".join(random.sample(lower+upper+number+symbol,6))