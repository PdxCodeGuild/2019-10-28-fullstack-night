import datetime
rain_data_file = 'nw_portland_rain_data.txt'
#define function to read the raw data
def read_rain_data(rain_data_file):
    with open(rain_data_file) as rain_data_raw:
        #user readlines() to split into a list of lines
        lines = rain_data_raw.readlines()
    #establish rows which are lines stripped of whitespace, \n, etc
    rows = []
    for line in lines:
        row = line.strip()
        rows.append(row)
    # print(rows)
    #below is finding the '------' line and popping each row above it
    count = 0
    for row in rows:
        rows.pop(count)
        # print(pop_row)
        if row == '-' * len(row):
            break
        count += 1
    rows = rows[count:]

    # print(rows[::-1])
    #here I start with an empty list and fill it with dictionaries of one key/value pair: date and total rainfall
    date_and_rain_data = []
    for row in rows:
        date_and_rain = {}
        columns = row.split()
        try:
            date_and_rain[columns[0]] = int(columns[1])
        except:
            date_and_rain[columns[0]] = columns[1]
            # print(date_and_rain)
        # date_and_rain = dict(zip(columns[0], columns[1]))
        date_and_rain_data.append(date_and_rain)
    return date_and_rain_data
# read_rain_data('nw_portland_rain_data.txt')
print(read_rain_data('nw_portland_rain_data.txt'))


date_and_rain_data = read_rain_data(rain_data_file)

def find_mean(date_and_rain_data):
    sum = 0
    days = 0
    for date_and_rain in date_and_rain_data:
        try:
            sum_plus = list(date_and_rain.values())
            sum += sum_plus[0]
            days += 1
        except:
            continue
    mean = sum / days
    return mean
mean = find_mean(date_and_rain_data)
print(f"daily mean is {mean*.01} in")

def find_variance(mean, date_and_rain_data):
    sum = 0
    days = 0
    for date_and_rain in date_and_rain_data:
        try:
            sum_plus = list(date_and_rain.values())
            sum += (sum_plus[0] - mean) ** 2
            days += 1
        except:
            continue
    variance = sum / days
    return variance
variance = find_variance(mean, date_and_rain_data)
print(f"Daily variance is {variance*0.01} in")

#find the day which had the most rain
def rainiest_day(date_and_rain_data):
    totals_list = []
    for date_and_rain in date_and_rain_data:
        dumb_extra_step_there_should_be_some_other_better_way_of_doing_but_i_dont_know_it_so_im_doing_this = list(date_and_rain.values())
        totals_list.append(dumb_extra_step_there_should_be_some_other_better_way_of_doing_but_i_dont_know_it_so_im_doing_this[0])
    # print(totals_list)
    totals_list = [x for x in totals_list if x != '-']
    most_rain = max(totals_list)
    rainiest_days = []
    for date_and_rain in date_and_rain_data:
        rain = list(date_and_rain.values())
        date = list(date_and_rain.keys())
        if rain[0] == most_rain:
            rainiest_days.append(date[0])
    return most_rain, rainiest_days
most_rain, rainiest_days = rainiest_day(date_and_rain_data)
print(f"The rainiest day(s) was/were {rainiest_days} with {most_rain*0.01} in")

#function to convert to datetime
def get_date_time(date_and_rain_data):
    datetime_list = []
    for date_and_rain in date_and_rain_data:
        new_dict = {}
        key_step1 = list(date_and_rain.keys())
        key_step2 = key_step1[0]
        date = datetime.datetime.strptime(key_step2, '%d-%b-%Y')
        new_key = (date.year, date.month, date.day)
        value_step1 = list(date_and_rain.values())
        value_step2 = value_step1[0]
        new_dict[new_key] = value_step2
        datetime_list.append(new_dict)
    return datetime_list
datetime_list = get_date_time(date_and_rain_data)
print(datetime_list)

#find the year which had the most rain on average
for date_and_rain in datetime_list:
    key_step1 = list