class employee:
    language = "py"
    salary = 1200000

    def getInfo(self):
        print(f"MY language is {self.language}. salary is  {self.salary}")

    # def __init__(self):  #dunder Method which is automatically called u don't need to call this method separately
    #     # print("i aM CREATING AN OBJECT COz I DONT NEED ANOTHER OBJECT TO CREATE OBJECT")
    #     print(f"The language is {self.language}. The salary is {self.salary}")

    def __init__(self, name, language, salary):
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")


    @staticmethod 
    def greet():  #abb ye ek function hai
        print("Good morning")


harry = employee("Sayma", 1300000, "JavaScript")
# harry.name = "harry"
print(harry.name, harry.language, harry.salary)


# rohan = employee()