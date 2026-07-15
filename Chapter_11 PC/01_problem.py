class TwoDVector:
    def __init__(self, i, j):  # yr automaticallyu chalta hai ise constructor method kahte hai
        self.i = i
        self.j = j

    def show(self):
        print(f"The vector is {self.i}i + {self.j}j ")


# __init__() = Object banne ke time ki taiyari (initialization).
# show() = Object se baad me koi kaam karwana (display, calculation,update etc)




class ThreeDVector(TwoDVector):
    def __init__(self, i,j,k):
        super().__init__(i, j)
        self.k = k


    def show(self):       #ye instance method hai
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")

                 
a = TwoDVector(1,2)
a.show()
b = ThreeDVector(6,3,4)
b.show()
