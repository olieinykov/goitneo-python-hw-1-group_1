def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def upsert_contact(args, contacts):
    name, phone = args
    contacts[name] = phone


def add_contact(*args):
    upsert_contact(*args)
    return "Contact added."


def change_contact(*args):
    upsert_contact(*args)
    return "Contact updated."


def get_contacts_phonenumber(name, contacts):
    contact = contacts.get(name[0].lower())

    if contact:
        print(contact)
    else:
        print("User with such number not exist.")


def get_all_contacts(contacts):
    for key, value in contacts.items():
        print(f"{key}: {value}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contacts_phonenumber(args, contacts))
        elif command == "all":
            print(get_all_contacts(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
