"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name, salary = 0, contract_hours = 0, contract_pay_per_hour = 0, contract_comm = 0, num_of_contract_comm = 0, bonus = 0):
        self.name = name
        self.salary = salary
        self.contract_hours = contract_hours
        self.contract_pay_per_hour = contract_pay_per_hour
        self.contract_comm = contract_comm
        self.num_of_contract_comm = num_of_contract_comm
        self.bonus = bonus

    def get_pay(self):
        total = 0
        if self.salary:
            total += self.salary
        else:
            total += self.contract_hours * self.contract_pay_per_hour

        if self.bonus:
            total += self.bonus

        if self.contract_comm:
            total += self.contract_comm * self.num_of_contract_comm

        return total

    def __str__(self):
        statement = self.name

        if self.salary:
            statement += (
                ' works on a monthly salary of ' + str(self.salary)
            )
        else:
            statement += (
                ' works on a contract of ' + str(self.contract_hours) + ' hours '
                + 'at ' + str(self.contract_pay_per_hour) + '/hour'
            )

        if self.contract_comm:
            statement += (
                ' and receives a commission for '
                + str(self.num_of_contract_comm)
            )
            if self.num_of_contract_comm > 1:
                statement += ' contract(s)'
            else:
                statement += ' contract'

            statement += ' at ' + str(self.contract_comm) + '/contract'

        if self.bonus:
            statement += ' and receives a bonus commission of ' + str(self.bonus)

        statement += '.  Their total pay is ' + str(self.get_pay()) + '.'

        return statement


'''Workers on a salary contract without commission.'''
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

'''Workers on an hourly contract without commission.'''
# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract_hours=100, contract_pay_per_hour=25)

'''Workers on a salary contract with a contract commission.'''
# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary = 3000, contract_comm=200, num_of_contract_comm=4)

'''Workers on an hourly contract with a contract commission.'''
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contract_hours=150, contract_pay_per_hour=25, contract_comm=220, num_of_contract_comm=3)

'''Workers on an salary contract with a bonus commission.'''
# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary = 2000, bonus = 1500)

'''Workers on an hourly contract with a bonus commission.'''
# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract_hours=120, contract_pay_per_hour=30, bonus = 600)

print(billie.__str__())
print(charlie.__str__())
print(renee.__str__())
print(jan.__str__())
print(robbie.__str__())
print(ariel.__str__())
