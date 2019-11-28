import string
import datetime
import re
import statistics

def get_data(rain_data):
    with open(rain_data) as rain_text:
        text = rain_text.readlines() # reallines returns a list split along new lines
        return text

# print(get_data("madison_rain.txt"))
filtered_list = []
date_total = []

data_list = get_data("madison_rain.txt")
data_filter = re.compile("\d{2}-[a-zA-Z]{3}-\d{4} \d")

# print(data_list[0])

for line in data_list:
    if line.startswith(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
        filtered_list.append(line.split())

key = ['date', 'total']
list_of_dictionaries = []

for index in filtered_list:
    one_dict = {}
    one_dict[key[0]] = index[0]
    one_dict[key[1]] = index[1]
    list_of_dictionaries.append(one_dict)

# print(list_of_dictionaries[:20])
for datum_date in list_of_dictionaries:
    datum_date["date"] = datetime.datetime.strptime((datum_date["date"]), '%d-%b-%Y')
    #print(datum_date)

#print(len(list_of_dictionaries)) # = 3639
totals_ints = []

for totals in list_of_dictionaries:
    if totals["total"] != "-":
        totals["total"] = int(totals["total"])
        totals_ints.append(totals["total"])

print(totals_ints)
print(max(totals_ints))
total_mean = statistics.mean(totals_ints)

print(total_mean)

# print(totals_ints[0], totals)
#
# print(type(list_of_dictionaries[0]['date']))

# Formatting Example
# for datum in data:
#     datum['date'] = datum['date'] + 'AL'

#print(date)


# print(filtered_list)

# for x, y in filtered_list:
#
#
# print(filtered_list[0][0], filtered_list[0][1])


# print(re.findall(data_filter, data_list))

#print(day_mo_yr_data)

#data_list = re.findall(data_filter, text)
#print(data_list)
#
# for line in text[:25]:
#     if not line.startswith("%d-%b-%Y"):
#         line = text.pop()
#     elif line.startswith("%d-%b-%Y"):
#         data_list.append(line)
#         print(data_list)

"""Formatting Example:
info = []
for one_line in data:
    if not one_line.startswith('.'):
        info.append(one_line.split()) # Adds lines without the dot '.' to a list

print(data[i:])"""


# Note: there is a function for checking ".startswith('-')"
# Look up "python enumerate(data)"

# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
