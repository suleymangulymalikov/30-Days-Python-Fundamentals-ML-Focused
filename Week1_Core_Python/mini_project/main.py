from contact import Contact

if __name__ == "__main__":
    contact = Contact()

    contact.add("Suleyman", "+48 123 234 345")
    contact.add("Youseff", "+48 123 234 345")
    contact.add("Yakup", "+48 123 234 345")
    contact.add("Ahmed", "+48 123 234 345")

    contact.update("Suleyman", "+48 987 765 432")

    contact.remove("Ahmed")

    contact.allContacts()

    contact.searchContact("Suleyman")