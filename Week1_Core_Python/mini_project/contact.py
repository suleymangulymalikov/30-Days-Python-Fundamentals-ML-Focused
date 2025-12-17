class Contact:
    def __init__(self):
        self.contacts = dict()

    def add(self, name, phone_number):
        self.contacts[name] = phone_number
        print(f"Added new contact: {name}: {phone_number}")

    def update(self, name, new_phone_number):
        old_phone_number = self.contacts[name]
        self.contacts[name] = new_phone_number
        print(f"Updated {name} contact from {old_phone_number} to {new_phone_number}")

    def remove(self, name):
        self.contacts.pop(name)
        print(f"Removed {name}'s contact")

    def allContacts(self):
        print("All Contacts")
        for (name, phone_number) in self.contacts.items():
            print(f"Name: {name}  Phone Number: {phone_number}")

    def searchContact(self, name):
        if name in self.contacts:
            print("Contact Found")
            print(f"Contact Information. \nName: {name}  Phone Number: {self.contacts[name]}")
        else:
            print("Contact not found")

