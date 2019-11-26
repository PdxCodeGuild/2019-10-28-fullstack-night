
with open('contacts.csv', 'r') as person:
    rows = person.read().split('\n')

headers = rows[0]
header_list = headers.split(',')


person_list = []
for person in rows[1:]:
    row_list = person.split(',')
    person_dict = {}
    for i in range(len(row_list)):
        person_dict[header_list[i]] = row_list[i]
    
    person_list.append(person_dict)

print(f"person_list {person_list}")