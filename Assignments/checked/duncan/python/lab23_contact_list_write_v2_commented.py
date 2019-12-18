contacts = []

with open("contacts.csv") as f:
    csv_data = f.read()
    rows = csv_data.split("\n")
    headers = rows[0].split(",")

    for row in rows[1:]:
        if not row: # nice, catching the empty string
            continue 
        else:
            values = row.split(",")
            contact_dictionary = dict(zip(headers, values))
            #print(contact_dictionary)
            contacts.append(contact_dictionary)

    print(contacts[0]["name"])

    program_running = "True"

    while program_running == "True":


        user_action = input("What action do you wish to perform? Create, Retreive, Update, Delete, or Quit: ").lower()



        if user_action not in ["create", "retreive", "update", "delete", "quit"]:
            print("Invalid Action")
            continue

        if user_action == "create":
            user_name = input("What is your name? ")
            user_phone = input("What is your phone number? ")
            user_email = input("What is your email address? ")
            user_address = input("What is your home address? ")


            user_info = (f"{user_name},{user_phone},{user_email},{user_address}")

            user_list = user_info.split(",")
            # user_list = [user_name, user_phone, user_email, user_address]
            user_dict = dict(zip(headers, user_list))
            contacts.append(user_dict)
            print(contacts)

        elif user_action == "retreive":
            user_lookup = input(f"Which user's information do you want to {user_action}? ")
            for index, contact in enumerate(contacts):
                if contact["name"] == user_lookup:
                    break

            print(index, contact) # this will give the last one if it can't be found.
            # you could set a boolean flag, found=False, and then set found=True if a contact matches
            # then only print if the flag is set to True


        elif user_action == "update":
            user_lookup = input(f"Which user's information do you want to {user_action}? ")
            key = input(f"Which attribute do you want to update?\nname, phone number, email address, or home address: ") # NEED TO CREATE CASE FOR INVALID
            value = input("What do you want the new attribute to be? ")

            for index, contact in enumerate(contacts):
                if contact["name"] == user_lookup:
                    contacts[index][key] = value
                    break

            print(index, contacts) # nice!

        elif user_action == "delete":
            user_lookup = input(f"Which user's information do you want to {user_action}? ")
            for index, contact in enumerate(contacts):
                if contact["name"] == user_lookup:
                    contacts.pop(index)
                    break

            print(index, contacts) # nice!

        elif user_action == "quit":
            csv_data = f.write() # THIS IS NOT WORKING
            program_running = "False"
