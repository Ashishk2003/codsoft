import json

CONTACT_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACT_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_contacts(contacts):
    with open(CONTACT_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    address = input("Enter address: ").strip()
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return
    print("\nContact List:")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}")

def search_contact(contacts):
    search_term = input("Enter name or phone number to search: ").strip()
    results = {name: info for name, info in contacts.items() if search_term in (name, info['phone'])}
    
    if not results:
        print("No contacts found.")
        return
    
    print("\nSearch Results:")
    for name, info in results.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}, Address: {info['address']}")

def update_contact(contacts):
    """Update an existing contact."""
    name = input("Enter the name of the contact to update: ").strip()
    if name not in contacts:
        print(f"No contact found with the name '{name}'.")
        return

    print(f"Updating contact '{name}'.")
    phone = input("Enter new phone number (leave blank to keep current): ").strip()
    email = input("Enter new email address (leave blank to keep current): ").strip()
    address = input("Enter new address (leave blank to keep current): ").strip()

    if phone:
        contacts[name]['phone'] = phone
    if email:
        contacts[name]['email'] = email
    if address:
        contacts[name]['address'] = address

    save_contacts(contacts)
    print(f"Contact '{name}' updated successfully!")

def delete_contact(contacts):
    """Delete an existing contact."""
    name = input("Enter the name of the contact to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact '{name}' deleted successfully!")
    else:
        print(f"No contact found with the name '{name}'.")

def main():
    """Main function to manage the contact book."""
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option (1-6): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the contact book. Goodbye!")
            break
        else:
            print("Invalid option. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main()
