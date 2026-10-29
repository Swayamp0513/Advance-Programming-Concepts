def calculate_gross(basic, hra_rate=0.2, da_rate=0.5):
    return basic + (basic * hra_rate) + (basic * da_rate)

def calculate_deductions(gross, pf_rate=0.12, tax_rate=0.05):
    return (gross * pf_rate) + (gross * tax_rate)

def calculate_net(basic):
    gross = calculate_gross(basic)
    deductions = calculate_deductions(gross)
    return gross - deductions
