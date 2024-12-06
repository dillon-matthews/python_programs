import pickle
import random

filename = "names_emails.dat"

def load_data():
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}

def save_data(data):
    with open(filename, "wb") as file:
        pickle.dump(data, file)

def display_menu():
    print("1. Look up an email address")
    print("2. Add a new name and email address")
    print("3. Change an existing email address")
    print("4. Delete an existing name and email address")
    print("5. Exit")

def lookup_email(data):
    name = input("Enter the name: ")
    email = data.get(name, "Not found")
    print(f"Email: {email}")

def add_entry(data):
    name = input("Enter the name: ")
    if name in data:
        print("Name already exists.")
    else:
        email = input("Enter the email address: ")
        data[name] = email

def change_email(data):
    name = input("Enter the name: ")
    if name in data:
        email = input("Enter the new email address: ")
        data[name] = email
    else:
        print("Name not found.")

def delete_entry(data):
    name = input("Enter the name: ")
    if name in data:
        del data[name]
    else:
        print("Name not found.")

data = load_data()

if not data:
    data = {
        "Alice Johnson": "alice.johnson@example.com",
        "Bob Smith": "bob.smith@example.com",
        "Catherine Jones": "catherine.jones@example.com",
        "David Brown": "david.brown@example.com",
        "Evelyn Miller": "evelyn.miller@example.com",
        "Frank Harris": "frank.harris@example.com",
        "Grace Martin": "grace.martin@example.com",
        "Hannah Moore": "hannah.moore@example.com",
        "Ian White": "ian.white@example.com",
        "Jane Lee": "jane.lee@example.com",
        "Kevin Garcia": "kevin.garcia@example.com",
        "Laura Walker": "laura.walker@example.com",
        "Michael Hall": "michael.hall@example.com",
        "Nina Young": "nina.young@example.com",
        "Oliver Allen": "oliver.allen@example.com"
    }

while True:
    display_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        lookup_email(data)
    elif choice == "2":
        add_entry(data)
    elif choice == "3":
        change_email(data)
    elif choice == "4":
        delete_entry(data)
    elif choice == "5":
        save_data(data)
        break
    else:
        print("Invalid choice. Try again.")
