def get_contacts(contacts_file):
  with open(contacts_file) as contacts_file:
    lines = contacts_file.readlines()
    headers = lines.pop(0).strip().split(',')

    contacts = []

    for line in lines:
      columns = line.strip().split(',')

      # Manual way:
      # contact = {}
      # for i in range(len(headers)):
      #   contact[headers[i]] = columns[i]
      # Fancy Python way:
      contact = dict(zip(headers, columns))
      contacts.append(contact)

  return headers, contacts

headers, contacts = get_contacts("contacts.csv")

actions = ["create", "retrieve", "update", "delete", "quit"]

while True:
  action = input("What would you like to CRUD? Or quit! ").casefold()

  # Check for a valid action
  if action not in actions:
    print("Please enter a valid action!")
    continue

  # Check if they're quitting
  if action == "quit":
    print("Thanks for stealing people's information!")
    break

  # If they're creating a contact 
  if action == "create":
    new_contact = {}
    # Ask them to input a value for each header from our csv and assign it to a new dictionary
    for header in headers:
      new_contact[header] = input(f"{header.capitalize()}: ")
    
    contacts.append(new_contact)
  elif action == "retrieve":
    search_name = input("Who would you like to retrieve? ").casefold()

    # Find a contact with a matching name
    for contact in contacts:
      if contact['name'] == search_name:
        break
    
    # Print each key value pair from the contact dict
    for header in headers:
      contact[header] = print(f"{header.capitalize()}: {contact[header]}")

  elif action == "update":
    search_name = input("Who would you like to edit? ").casefold()

    # Find a contact with a matching name
    for contact in contacts:
      if contact['name'] == search_name:
        break
      
    # Update each key value pair in the dict with the users input
    for header in headers:
      value = input(f"{header.capitalize()} ({contact[header]}): ")
      if value: 
        contact[header] = value

    contacts.append(contact)

  elif action == "delete":
    search_name = input("Who would you like to delete? ").casefold()

    # Find a contact with a matching name
    for i, contact in enumerate(contacts):
      if contact['name'] == search_name:
        break
      
    # Pop it from the list
    contacts.pop(i)

