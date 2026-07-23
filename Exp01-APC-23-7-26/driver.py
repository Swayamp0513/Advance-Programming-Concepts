print("Enter the Driver Detailes:")
age = int(input("1.Enter Drivers Age:"))
g = input("2.Enter Gender(M or F):")
md = input("3.Enter Whether Driver is Married(Y) or Not Married(N):")
if (md == "Y"):
    print("Driver is insured.")
elif (md == 'N') and (g == 'M') and (age > 30):
    print("Driver is insured.")
elif (md == 'N') and (g == 'F') and (age > 25):
     print("Driver is insured.")
else :
    print("Driver is not insured.")

