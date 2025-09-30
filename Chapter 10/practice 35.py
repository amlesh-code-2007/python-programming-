# write a class train which has methods to book a ticket, get status(no of seats) and gets fare information of trainrunning under indian Railways...

from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticked is booked in tain no: {self.trainNo} from {fro} to {to}")

    def getStatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getFire(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)}")


t = Train(12564)
t.book("Rampur", "Delhi")
t.getStatus()
t.getFire("Rampur","Delhi")