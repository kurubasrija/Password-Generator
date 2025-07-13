contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"✅ Contact for {name} added.")

def view_contacts():
    if not contacts:
        print("📭 No contacts to show.")
    else:
        for name, info in contacts.items():
            print(f"\n📇 Name: {name}")
            print(f"📞 Phone: {info['Phone']}")
            print(f"📧 Email: {info['Email']}")

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"\n📇 Name: {name}")
        print(f"📞 Phone: {contacts[name]['Phone']}")
        print(f"📧 Email: {contacts[name]['Email']}")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"🗑️ Contact for {name} deleted.")
    else:
        print("❌ Contact not found.")

def menu():
    while True:
        print("\n📱 Contact Book Menu")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")

menu()
