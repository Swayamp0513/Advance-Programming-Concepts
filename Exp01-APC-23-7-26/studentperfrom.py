M1= int(input("Enter Student Marks of Subject1(out of 100):"))
M2= int(input("Enter Student Marks of Subject2(out of 100):"))
M3= int(input("Enter Student Marks of Subject3(out of 100):"))
M4= int(input("Enter Student Marks of Subject4(out of 100):"))
Per = ((M1+M2+M3+M4)/400)*100
print("Total Percenetage:",Per)
if Per>=90:
    print("Excellent Performane.")
elif Per>=80:
    print("Very Good Performane.")
elif Per>=70:
    print("Good Performane.")
elif Per>=60:
    print("Average Performane.")
else:
    print("Poor Performane.")

