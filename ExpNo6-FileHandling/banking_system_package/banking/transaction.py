def deposit(acc, amt):
    acc["balance"] += amt
    return acc["balance"]
def withdraw(acc, amt):
    if acc["balance"] >= amt:
        acc["balance"] -= amt
        return acc["balance"]
    return "Insufficient Funds"
