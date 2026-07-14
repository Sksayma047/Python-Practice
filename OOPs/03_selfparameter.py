class employee:
    language = "py"
    salary = 1200000

    

    def getInfo(self):
        print(f"MY language is {self.language}. salary is  {self.salary}")


    @staticmethod 
    def greet():  #abb ye ek function hai
        print("Good morning")


harry = employee()
harry.name = "harry"
harry.getInfo()
harry.greet()
# employee.getInfo(harry)
print( harry.language, harry.salary)
