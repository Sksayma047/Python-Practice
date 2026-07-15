class Employee:
    a = 1
class Programmer(Employee):
    b = 2
    pass
class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)
# print(o.b)  # This will raise an AttributeError since 'Employee' object has no attribute 'b' 

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c)