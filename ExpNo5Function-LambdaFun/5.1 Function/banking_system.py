balance = 0.0
history = []
def deposit(amount):
    global balance
    balance += amount
    history.append(f"Deposited: {amount}")
def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        history.append(f"Withdrew: {amount}")
def get_balance():
    return balance

def get_history():
    return history

deposit(1000)
withdraw(300)
withdraw(1000)
print("Current Balance:", get_balance())
print("History:", get_history())
