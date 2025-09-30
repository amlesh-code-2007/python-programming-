# write a class "calculator" capable of finding square, cube and square root of a number....

class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"the square is {self.n*self.n}")
              
    def cube(self):
        print(f"the cube is {self.n*self.n*self.n}")

    def squareroot(self):
        print(f"the squareroot is {self.n**1/2}")

    @staticmethod
    def hello():
        print("Hello World!")
       

a = calculator(9)
a.hello()
a.square()
a.cube()
a.squareroot()