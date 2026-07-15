class Number:
    def __init__(self, n):
        self.n = n
    
    def __add__(self,num):
        return self.n + num.n
    
n = Number(10)
m = Number(10)

print(n + m)


#in py language opraters are writen like this
# p1+p2 p1.__add__(p2)
# p1-p2 p1.__sub__(p2)
# p1*p2 p1.__mul__(p2)
# p1/p2 p1.__truediv__(p2)
# p1//p2 p1.__floordiv__(p2)

# dunder method  = __str__() used to set what gets displayed upon calling str(obj)
#__len__() used to set what gets displayed upon calling. __len__() or len(obj)