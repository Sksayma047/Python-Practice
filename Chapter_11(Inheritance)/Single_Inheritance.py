class Employee:
    company = "ITC"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print(f"The name of the Employee is {self.name}, company is {self.company} and the salary is {self.salary}")





class Programmer(Employee):
    company = "ITC Infotech"
    def __init__(self, name, salary, language):
        super().__init__(name, salary) # aisa super() use karke bhi likh sakte hai
        # self.name= name  #aisa bhi likh sakte
        # self.salary = salary
        self.language = language

    def showLanguage(self):
        print(f"The name of the Programmer is {self.name}, company is {self.company}, salary is {self.salary} and the language is {self.language}")


a = Employee("Rahul", 10000)
a.show()

b = Programmer("Sayma", 1200000, "Python")
b.showLanguage()