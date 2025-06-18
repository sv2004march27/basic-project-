contact = {}
while True:
    print("\n contact book app")
    print("1. create a contact ")
    print("2. View Contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Search Contact")
    print("6. count contact")
    print("7. Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        name = input("Enter your name: ")
        if name in contact:
            print("contact name already exists")
        else:
            age = int(input("enter your age:"))
            E_mail = input("enter your E-mail: ")
            mobile = input("enter your mobile: ")
            contact[name]={"age":int(age),"email":E_mail,"mobile":mobile,"mobile":mobile}
            print(f"contact name {name} has been created sucessfully!")
    elif choice == "2":
        name = input("enter contact name to view =")
        if name in contact:
            contact = contact[name]
            print(f"Name:{name},Age:{age}, MobileNumber:{mobile}")
        else:
            print("contact not found")
    elif choice == "3":
        name = input("enter name to update contact=")
        if name in contact:
            age = input("enter update age =")
            E_mail = input("enter update E-mail=")
            mobile = input("enter update mobile=")
            contact[name]= {"age":int(age),"mobile":mobile,"mobile":mobile}
        else:
            print("contact not found")
    elif choice == "4":
        name = input("Enter contact name to delete=")
        if name in contact:
            del contact[name]
        print(f"contact name {name} has been deleted!")
    elif choice == "5":
        search_name = input("Enter contact name to search=")
        found = False
        for name , contact in contact .items():
            if search_name.lower() in name.lower():
                print(f"Found - Name {name}, Age:{age},Mobile Number:{mobile}, Email:{E_mail}")
                found = True
    if not found:
        print("No such contact found")
    elif choice == "6":
        print(f"Total contacts in your book: {len(contact)}")
    elif choice == "7":
        print("Goodbye! Closing the application...")
        break
    else:
        print("Invalid choice. Please try again.")
