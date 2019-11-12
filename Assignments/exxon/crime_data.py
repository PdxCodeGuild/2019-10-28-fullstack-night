import csv 

from collections import Counter 
from datetime import datetime

most_common_crimes = []
new_most_crimes = {}
crime_frequency = {}
report_date_list = []
year_only_dates = []



f = open('crime_data.csv')
csv_f = csv.reader(f)

for row in csv_f:
    crimes_list = (row[3])
    most_common_crimes.append(crimes_list)
    
# print (most_common_crimes)
    

for item in (most_common_crimes):
    if item in new_most_crimes:
        new_most_crimes [item] +=1
    else:
        new_most_crimes [item] =1 

print("\n")
print("Crime list with number of ocurrances:" '\n')
print(new_most_crimes)





#  using counter to parse through crimes dictionary and find most occuring crime type 

k = Counter(new_most_crimes)


high = k.most_common(1)

for i in high: 
    most_common_winner = i[0] , i[1] 


#  using counter to parse through crimes dictionary and find least occuring crime type 

l = Counter(new_most_crimes)


lowest = l.most_common()[:-2:-1]

for i in lowest: 
    least_common_winner = i[0] , i[1] 






f.close()




f = open('crime_data.csv')

csv_f = csv.reader(f)
for row in csv_f:
    dates_list = (row[1])
    report_date_list.append(dates_list)
    




# take list of dates and convert to datetime objects then convert back to string parsing out only the year

for line in report_date_list[1:]:
   x = (datetime.strptime(line,"%m/%d/%Y").date())
   x = (datetime.strftime(x, "%Y"))
   year_only_dates.append(x)



# parsing through list of years for year with most occurances  

p = Counter(year_only_dates)


most_occ_year = p.most_common(1)

for i in most_occ_year: 
    most_common_year = i[0]  





print('\n')
print('\n')


print("According to this csv file:" "\n") 
print(f"The most common crime type is : {most_common_winner[0]} with {most_common_winner[1]} occurances " '\n')
print(f"The least common crime type is : {least_common_winner[0]} with {least_common_winner[1]} occurance " '\n')
print(f"The year with the most crime was {most_common_year}")

print('\n')
f.close()   