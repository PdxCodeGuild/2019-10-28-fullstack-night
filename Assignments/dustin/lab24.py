'''
By: Dustin DeShane
Filename: lab24.py
'''
import datetime
import string

sum_count = 0
count = 0
list_full = []
current_high = 0
#new_value = 0
year_count = 2019
counter = {}
highest_year = 0
high_avg_amt = 0

with open('ankeny.rain.txt', 'r') as rain_data:
    data = rain_data.read().split('\n')
    my_sum = 0
    count = 0
    for i in data[:100]:
        count += 1
        if i.endswith("----"):
            break
    for i in data[count:]:
        if i:
            parsed = i.split()
            set_tuple = (parsed[0], parsed[1])
            list_full.append(set_tuple)

            # parse date #
            date = datetime.datetime.strptime(parsed[0], '%d-%b-%Y')
            year = date.year
            day = date.day
            month = date.month
            #print(year, month)
            # done parsing date #

                

            if parsed[1].isdigit():
                if year not in counter:
                    counter[year] = int(parsed[1])
                else:
                    counter[year] += int(parsed[1])
                
                    
                

                

                if int(parsed[1]) > current_high:
                    current_high = int(parsed[1])
                    date_store = parsed[0]
                # my_sum += int(parsed[1])
                # sum_count += 1
                
    for i in counter:
        if counter[i] > high_avg_amt:
            highest_year = i
            high_avg_amt = counter[i] 
        else:
            continue   
    print(highest_year, high_avg_amt)        
    #print(date_store, current_high)
    #print(counter)
    #print(max(counter.values()))
    


    # my_avg = my_sum/sum_count

    # print(sum_count)
    # print(my_sum)
    # print(my_avg)
    #print(list_full)


    