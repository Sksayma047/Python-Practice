class Employee:
    a = 1
class Programmer(Employee):
    b = 2
    pass
class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)