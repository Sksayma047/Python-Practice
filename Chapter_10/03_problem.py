from random import randint
class train:

    def __init__(self, trainNo):
        self.trainNo = trainNo
    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Ticket fare in trainn no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")


t = train(12345)
t.book("Dhaka", "Chittagong")
t.getstatus()
t.getfare("Dhaka", "Chittagong")
