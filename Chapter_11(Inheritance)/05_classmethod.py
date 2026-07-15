class Employee:
    a = 1
#if we are not using decorater and instance changes the value the instance value will be output
    @classmethod  #by using classmethod decorator we can access class variable without creating object of class
    def show(cls): # it use class variable value insted of instance variable value, it uses cls apart from self
        print(f"This is employee class {cls.a}")

e = Employee()
e.a = 45
e.show()
