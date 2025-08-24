contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print("Contact added.")

    elif choice == '2':
        if not contacts:
            print("No contacts found.")
        else:
            for name, phone in contacts.items():
                print(f"{name}: {phone}")

    elif choice == '3':
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"{search_name}: {contacts[search_name]}")
        else:
            print("Contact not found.")

    elif choice == '4':
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")
