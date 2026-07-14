class Employee:
    company = "Microsoft"
    name = "Deafult name"
    def show(self):
        print(f"The company of employee is {self.company} and name is {self.name}")

class Programmer:
    language = "python"
    def printLanguage(self):
        print(f"Thae language of programmer is {self.language} and he loves to code in {self.language}")
    

class Freelancer(Employee, Programmer):
    company = "ITC Infotech"
    def showAll(self):
        print(f"The company of freelancer is {self.company} and his name is {self.name} ")


a = Employee() 
b = Programmer()
c = Freelancer()
# a.show()
# b.printLanguage()
# c.showAll()

c.show()
c.printLanguage()
c.showAll()
