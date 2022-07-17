from functools import reduce
def add(x, y) :
    return x +" "+ y
words = ['I', 'have', 'a', 'dream'] 
sum1 = reduce(add,words)
print(sum1,end=" ")