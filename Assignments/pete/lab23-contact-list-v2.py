'''
Lab 23: Contact List
Version2

Implement a CRUD REPL

    *Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
    *Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
    *Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
    *Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

'''
with open('cities_list.csv', 'r') as cities:
#establish the rows
    rows = cities.read().split('\n')
#find the header
headers = rows[0]
#split the headers into its own list
header_list = headers.split(',')
# print(f"rows {rows}")
# print(f"headers {headers}")
# print(f"header_list {header_list}")
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
print(f"cities_list {cities_list}")

####START VERSION 2

#create a record
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

#retrieve a record
user_retrieve = input("Enter City for info retrieval: ")
for city_dict in cities_list:
    if city_dict['City'] == user_retrieve:
        break

print(f"city_dict: {city_dict}")

#update a record
user_update_city = input("Which City would you like to update? ")
user_update_attribute = input("Which attribute would you like to update? ")
user_update_new_attribute = input("And what would you like to change it to? ")
for city_dict in cities_list:
    if city_dict['City'] == user_update_city:
        break
city_dict[user_update_attribute] = user_update_new_attribute

print(cities_list)

#delete a record
user_remove_city = input("Which city would you like to delete from the list? ")
for city_dict in cities_list:
    if city_dict['City'] == user_remove_city:
        break
cities_list.remove(city_dict)

print(cities_list)