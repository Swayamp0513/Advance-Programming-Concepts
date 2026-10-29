from banking.account import create_account, get_balance
from banking.transaction import deposit, withdraw
from banking.loan import calculate_emi

my_acc = create_account("Rajesh", 10000)
deposit(my_acc, 2500)
withdraw(my_acc, 1200)

print("Account Holder:", my_acc["name"])
print("Final Balance:", get_balance(my_acc))
print("Car Loan EMI (5L, 8.5%, 5 yrs): Rs.", calculate_emi(500000, 8.5, 5))
