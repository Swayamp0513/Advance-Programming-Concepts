def calculate_hospital_bill(consultation, lab, medicine, room_days, category):
    room_charge = room_days * 2000
    total = consultation + lab + medicine + room_charge
    discount = 0
    if category == "Senior Citizen":
        discount = total * 0.15
    elif category == "Insurance":
        discount = total * 0.20
    return total - discount




final_bill = calculate_hospital_bill(500, 1200, 800, 3, "Senior Citizen")
print("Hospital Bill:", final_bill)
