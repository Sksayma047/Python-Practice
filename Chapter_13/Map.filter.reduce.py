
l = [1,2,3,4,5]

from functools import reduce


# map Example
squre = lambda x:x*x
sqList = map(squre, l)
print(list(sqList))



#Filter Example
def even(n):
    if (n%2 == 0):
        return True
    return False

onlyEven= filter(even, l)
print(list(onlyEven))



#Reduce Example
def sum(a,b):
    return a + b
mul = lambda x,y:x*y

print(reduce(mul, l))
print(reduce(sum, l))
