def create_account(name, initial_balance=0.0):
    return {"name": name, "balance": initial_balance}
def get_balance(acc):
    return acc["balance"]
