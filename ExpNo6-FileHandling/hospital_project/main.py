from patient_mgmt.admit import admit_patient
from doctor_mgmt.schedule import get_doctor_duty
from billing.invoice import generate_hospital_invoice
from medical_records.history import get_past_record

print(admit_patient("P01", "Sanjay"))
print(get_doctor_duty("Dr. Deshmukh"))
print(get_past_record("P01"))
print("Final Bill: Rs.", generate_hospital_invoice(600, 1450))
