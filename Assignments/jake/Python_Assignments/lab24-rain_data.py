with open('rain_list.txt') as rain:
    data_lines = rain.readlines()

start_index = -1
for i, line in enumerate(data_lines):
    if not line.startswith('-'):
        start_index = i
        break

print(start_index)
if start_index >= 0:
    pass
    #print(data_lines[start_index:])

list_of_lists = []
for line in data_lines[start_index:]:
    print(line.split())
    list_of_lists.append(line.split())
#print(list_of_lists)


