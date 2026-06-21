#Jatra Tracker

jatras = []          #list

'''#sample dictionary

jatra1 = {                               
    "name": "Rato Machhindranath",
    "location": "Patan",
    "month": "Baishak",
    "visited": "Yes"
}
jatras.append(jatra1)
print(jatras)'''
 
 #-----FUNCTION------
def add_jatra():
    
    name = input("Enter Jatra Name: ")
    location = input("Enter Location: ")
    month = input("Enter Month: ")
    visited = input("Visited Status(Yes/No): ")
    
    jatra = {
        "name" : name,
        "location" : location,
        "month" : month,
        "visited" : visited,
    }
    
    jatras.append(jatra)


def view_jatra():
    if len(jatras) == 0:
        print("No jatras found!")
    else:
        for jatra in jatras:
            print("Found!")
            print(f"{'Name':<12} : {jatra['name']}")
            print(f"{'Location':<12} : {jatra['location']}")
            print(f"{'Month':<12} : {jatra['month']}")
            print(f"{'Visited':<12} : {jatra['visited']}")
            print("-------------------------")


def search_jatra():
    search_name = input("Enter Jatra Name: ")
    for jatra in jatras:
        if jatra["name"].lower() == search_name.lower():
            print("Found!")
            print(f"{'Name':<12} : {jatra['name']}")
            print(f"{'Location':<12} : {jatra['location']}")
            print(f"{'Month':<12} : {jatra['month']}")
            print(f"{'Visited':<12} : {jatra['visited']}")
            return
    print(" Jatra not found!")

    print("Jatra not found!")
    


for jatra in jatras:
    print("Name:", jatra["name"])
    print("Location:", jatra["location"])
    print("Month:", jatra["month"])
    print()

#-----MENU-----
while True:
    print("\n===== JATRA TRACKER =====")
    print("1. Add Jatra")
    print("2. View All Jatras")
    print("3. Search Jatra")
    print("4. Exit")

    choice = input("\nEnter choice (1-4): ")

    if choice == "1":
        add_jatra()
        print("Jatra added successfully!")
    elif choice == "2":
        view_jatra()
    elif choice == "3":
        search_jatra()
    elif choice == "4":
        print("Exited")
        break
    else:
        print("Invalid choice, try again!")