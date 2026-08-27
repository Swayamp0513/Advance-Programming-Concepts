def slab_charge(units):
    if units <= 100:
        return units * 4.0
    elif units <= 300:
        return 100 * 4.0 + (units - 100) * 6.0
    else:
        return 100 * 4.0 + 200 * 6.0 + (units - 300) * 8.0





def calculate_full_bill(units, discount=0):
    fixed_charge = 150.0
    energy_charge = slab_charge(units)
    tax = (energy_charge + fixed_charge) * 0.05
    subtotal = energy_charge + fixed_charge + tax
    return subtotal - discount

units = 250
print("Total Bill Amount:", calculate_full_bill(units, discount=50))
