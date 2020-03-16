import datetime
import string 


rain_dates = []

with open('hayden_island.txt') as f:
     contents = f.readlines()  # read the contents

for i, one_row in enumerate (contents[:20]):
    if one_row[:5] == "-" *5:
        print("got it ")
        print(i)
        break
one_row = contents[i+1].split()[:2]
one_dict = {}


print("date", one_row[0])
print("total", one_row[1])












