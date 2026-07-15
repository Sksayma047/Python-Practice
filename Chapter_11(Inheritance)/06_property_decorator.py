class Employee:   # - we call it encapsulation - where all working component are binded in one unit class
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter # this is a implimented function - we call Abstarction it hides implimented function and shows only essential elements
    def name (self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

e = Employee()
e.a = 45

e.name = "Sayma Shaikh"
print(e.fname, e.lname)

e.show()


