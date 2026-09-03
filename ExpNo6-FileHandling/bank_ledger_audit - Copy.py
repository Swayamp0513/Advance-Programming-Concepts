with open("transactions.txt", "w") as f:
    f.write("DEPOSIT,5000\nWITHDRAWAL,1200\nDEPOSIT,3000\nWITHDRAWAL,2500\nDEPOSIT,800\n")

deposits = 0.0
withdrawals = 0.0
transactions = []

with open("transactions.txt", "r") as f:
    for line in f:
        ttype, amt = line.strip().split(",")
        amount = float(amt)
        transactions.append(amount)
        if ttype == "DEPOSIT":
            deposits += amount
        elif ttype == "WITHDRAWAL":
            withdrawals += amount

print("Total Deposits: Rs.", deposits)
print("Total Withdrawals: Rs.", withdrawals)
print("Final Balance: Rs.", deposits - withdrawals)
print("Largest Transaction: Rs.", max(transactions))
