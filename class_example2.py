class Laptop:
    def __init__(self, name=None, company=None, cpu=None, price=None):
        self.name = name
        self.company = company
        self.cpu = cpu
        self.price = price

Ideapad320 = Laptop('Ideapad320', 'Lenovo', 'Core i7 10th', '300')

print(Ideapad320)
print(Ideapad320.name)