# contact_book.py

# Store contacts as a list of dictionaries
contacts = []


def add_contact():
    """Add a new contact to the list."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    print(f"\nContact '{name}' added successfully!\n")


def search_contact(name):
    """Search for a contact by name and return the matching dictionary."""
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def delete_contact(name):
    """Remove a contact by name."""
    for i, contact in enumerate(contacts):
        if contact["name"].lower() == name.lower():
            removed = contacts.pop(i)
            print(f"\nContact '{removed['name']}' deleted successfully!\n")
            return True
    print(f"\nContact '{name}' not found.\n")
    return False


def view_all():
    """Display all contacts in a formatted layout."""
    if not contacts:
        print("\nNo contacts found.\n")
        return

    print("\n" + "=" * 40)
    print("        ALL CONTACTS")
    print("=" * 40)

    for contact in contacts:
        print(f"Name:  {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print("-" * 40)

    print(f"Total contacts: {len(contacts)}\n")


def main():
    """Run the contact book menu."""
    while True:
        print("=" * 30)
        print("      CONTACT BOOK MENU")
        print("=" * 30)
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Delete Contact")
        print("4. View All Contacts")
        print("5. Exit")
        print("=" * 30)

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            name = input("Enter name to search: ").strip()
            result = search_contact(name)
            if result:
                print("\nContact found:")
                print(f"  Name:  {result['name']}")
                print(f"  Phone: {result['phone']}")
                print(f"  Email: {result['email']}\n")
            else:
                print(f"\nContact '{name}' not found.\n")

        elif choice == "3":
            name = input("Enter name to delete: ").strip()
            delete_contact(name)

        elif choice == "4":
            view_all()

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please choose 1-5.\n")


# Run the program
if __name__ == "__main__":
    main()