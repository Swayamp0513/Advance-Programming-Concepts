patients = (
    (101, "Aayan", 30, "A+"),
    (102, "Ram", 45, "B+"),
    (103, "Raj", 25, "A+"),
    (104, "Harsh", 60, "O-")
)
while True:
    print("\n--- PATIENT RECORDS ---")
    print("1. Display all records")
    print("2. Search for a patient by ID")
    print("3. Count total number of patients")
    print("4. Display patients with a specific blood group")
    print("5. Exit")
    choice = int(input("Enter your choice (1-5): "))
    if choice == 1:
        for p in patients:
            print("ID:", p[0], "| Name:", p[1], "| Age:", p[2], "| Blood Group:", p[3])
    elif choice == 2:
        search_id = int(input("Enter Patient ID to search: "))
        found = False
        for p in patients:
            if p[0] == search_id:
                print("Found:", p)
                found = True
                break
        if not found:
            print("Patient not found.")
    elif choice == 3:
        print("Total patients:", len(patients))
    elif choice == 4:
        bg = input("Enter blood group: ")
        found = False
        for p in patients:
            if p[3].upper() == bg.upper():
                print(p)
                found = True
        if not found:
            print("No patients found with blood group", bg)
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice, try again.")