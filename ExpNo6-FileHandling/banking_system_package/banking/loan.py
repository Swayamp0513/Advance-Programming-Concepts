def calculate_emi(principal, rate, years):
    r = (rate / 12) / 100
    n = years * 12
    emi = (principal * r * ((1 + r)**n)) / (((1 + r)**n) - 1)
    return round(emi, 2)
