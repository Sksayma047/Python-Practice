class Programmer:

    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name=name
        self.salary = salary
        self.pin = pin


p = Programmer("sayma", 1200000, 413512)
print(p.name, p.salary, p.company, p.pin)
r = Programmer("Rafi", 1000000, 413512)
print(r.name, r.salary, r.company,r.pin)