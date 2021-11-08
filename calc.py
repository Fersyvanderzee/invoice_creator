class Calculation:
    name = ''
    amount = 0
    tax = 0.09
    price_per_meal = 12.5
    price_inc_tax = 0
    price_ex_tax = 0
    groceries = 0

    def __init__(self, name, amount, groceries):
        self.name = name
        self.amount = amount
        self.price_inc_tax = amount * self.price_per_meal
        self.price_ex_tax = self.price_inc_tax / (self.tax + 1.00)
        self.groceries = groceries

    def return_values(self):
        return str(self.name) + ' | ' + str(self.amount) + ' | ' + str(round(self.price_ex_tax, 2))

    def return_tax_difference(self):
        tax_difference = self.price_inc_tax - self.price_ex_tax
        return tax_difference

    def return_groceries(self):
        return self.groceries

    def return_price_inc_tax(self):
        return self.price_inc_tax


c1 = Calculation('Dirty Sound Magnet', 10, 24)
c2 = Calculation('Zoete zin & Reservoir Dogs', 12, 24)
print(c1.return_values())
print(c2.return_values())
print('Tax: ' + str(round(c1.return_tax_difference() + c2.return_tax_difference(), 2)))
print('Groceries: ' + str(round(c1.return_groceries() + c2.return_groceries(), 2)))
print('Total invoice: ' + str(round((c1.return_price_inc_tax() + c2.return_price_inc_tax()) - (c1.return_groceries() + c2.return_groceries()), 2)))

