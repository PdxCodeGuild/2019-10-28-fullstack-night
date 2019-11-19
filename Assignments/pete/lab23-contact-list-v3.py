'''
Lab 23: Contact List
Version3

When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup contacts.csv because you likely won't write it correctly the first time.
'''

with open('cities_list.csv', 'r') as cities:
#establish the rows
    rows = cities.read().split('\n')
#find the header
headers = rows[0]
#split the headers into its own list
header_list = headers.split(',')
cities_list = []
#for each line other than the header
for city in rows[1:]:
    #get a list for each row
    row_list = city.split(',')
    city_dict = {}
    #for each item in the row list
    for i in range(len(row_list)):
        city_dict[header_list[i]] = row_list[i]
    cities_list.append(city_dict)
print(f"cities_list:\n{cities_list}")

####START VERSION 2

while True:
    #create a record
    new_city_yn = input("Add new city to list (Y/N)? ").lower()
    while True:
        if new_city_yn == 'n':
            break
        else:
            user_city = input("Enter City: ")
            user_country = input("Enter Country: ")
            user_landmark = input("Enter Landmark: ")
            user_food = input("Enter Food: ")

            user_list = [user_city, user_country, user_landmark, user_food]
            user_dict = {}
            for i in range(len(user_list)):
                user_dict[header_list[i]] = user_list[i]
            cities_list.append(user_dict)

            print(f"Updated list:\n{cities_list}")
            break

    #retrieve a record
    retrieve_city_yn = input("Retrieve City info (Y/N)? ").lower()
    while True:
        if retrieve_city_yn == 'n':
            break
        else:
            user_retrieve = input("Enter City for info retrieval: ")
            for city_dict in cities_list:
                if city_dict['City'] == user_retrieve:
                    break

            print(f"City info:\n{city_dict}")
            break

    #update a record
    update_yn = input("Update a city's info (Y/N)? ").lower()
    while True:
        if update_yn == 'n':
            break
        else:
            user_update_city = input("Which City would you like to update? ")
            user_update_attribute = input("Which attribute would you like to update? ")
            user_update_new_attribute = input("And what would you like to change it to? ")
            for city_dict in cities_list:
                if city_dict['City'] == user_update_city:
                    break
            city_dict[user_update_attribute] = user_update_new_attribute

            print(f"Updated List:\n{cities_list}")
            break

    #delete a record
    remove_city_yn = input("Would you like to remove a City from the list (Y/N)? ").lower()
    while True:
        if remove_city_yn == 'n':
            break
        else:
            user_remove_city = input("Which city would you like to delete from the list? ")
            for city_dict in cities_list:
                if city_dict['City'] == user_remove_city:
                    break
            cities_list.remove(city_dict)

            print(f"Updated List:\n{cities_list}")
            break
        
    again_yn = input("Would you like to change anything else (Y/N)? ").lower()
    if again_yn == 'n':
        break
save_changes = input("Save Changes (Y/N)? ").lower()
if save_changes == 'y':
    out_data = headers
    for row in cities_list:
        out_data += '\n'
        for header in header_list:
            out_data += row[header] + ','
        out_data = out_data[:-1]
    # print(out_data)




    with open('cities_list.csv', 'w') as cities:
        cities.write(out_data)
