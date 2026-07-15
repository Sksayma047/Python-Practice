class Animals():
    dog = "my Dogy"
    def showAll(self):
        print(f"i lovvvv {self.dog}")


class Pets(Animals):
    def __init__(self, breed):
        self.breed = breed

    def show(self):
        print(f"I like the {self.breed} breed of dog.")


class Dog(Pets):
    @staticmethod # when u use staticmethos decorater then it automatically print text but getting for parent variable text u need to use self and call in print() 
    def bark(): # def bark():
        print(f"Dog barking - Bhaw Bhaw! i like dog breed")
        #print(f"Dog barking - Bhaw Bhaw! i like {self.breed} dog breed")

p = Dog("Labrador")
p.showAll()
p.show()
p.bark()
