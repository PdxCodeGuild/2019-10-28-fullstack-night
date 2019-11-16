'''
Lab 23: Contact List
Version1

Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.
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
for city in rows[1:]:
    row_list = city.split(',')
    city_dict = {}
    for i in range(len(row_list)):
        city_dict[header_list[i]] = row_list[i]
    cities_list.append(city_dict)
print(f"cities_list {cities_list}")