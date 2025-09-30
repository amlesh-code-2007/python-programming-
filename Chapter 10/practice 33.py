# Create a class "Programmer" for string information of few programmers wroking at microsoft......

class programmer:
    compony = "microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin
    
p = programmer("Harry", 1200000, 300507)
print(p.name, p.salary, p.pin, p.compony)
a = programmer("Amlesh", 1300000, 300502)
print(a.name, a.salary, a.pin, a.compony)        