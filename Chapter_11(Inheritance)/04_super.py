class Employee:
    def __init__(self):
        print("Constructor of employee")

class Programmer(Employee):
    def __init__(self):
        super().__init__()
        print("Constructor of programmer")

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of manager")

a = Employee()
b = Programmer()
c = Manager()

