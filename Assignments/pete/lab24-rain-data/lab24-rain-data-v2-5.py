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
    count = 1
    for row in rows:
        # rows.pop(count)
        # print(pop_row)
        if row and row == '-' * len(row):
            break
        count += 1
    rows = rows[count:]

    # print(rows[::-1])
    #here I start with an empty list and fill it with dictionaries of one key/value pair: date and total rainfall
    date_and_rain_data = []
    for row in rows:
        date_and_rain = {}
        columns = row.split()
        date_and_rain['Date'] = columns[0]
        try:
            date_and_rain['Rain'] = int(columns[1])
        except:
            date_and_rain['Rain'] = columns[1]
            # print(date_and_rain)
        # date_and_rain = dict(zip(columns[0], columns[1]))
        date_and_rain_data.append(date_and_rain)
    return date_and_rain_data
# read_rain_data('nw_portland_rain_data.txt')
print(read_rain_data('nw_portland_rain_data.txt'))


date_and_rain_data = read_rain_data(rain_data_file)
#function to find mean
def find_mean(date_and_rain_data):
    sum = 0
    days = 0
    for date_and_rain in date_and_rain_data:
        try:
            sum += date_and_rain['Rain']
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
            sum += (date_and_rain['Rain'] - mean) ** 2
            days += 1
        except:
            continue
    variance = sum / days
    return variance
variance = find_variance(mean, date_and_rain_data)
print(f"Daily variance is {variance*0.01} in")

#find the day which had the most rain
def rainiest_days(date_and_rain_data):
    totals_list = []
    for date_and_rain in date_and_rain_data:
        totals_list.append(date_and_rain['Rain'])
    # print(totals_list)
    totals_list = [x for x in totals_list if x != '-']
    most_rain = max(totals_list)
    rainiest_days = []
    for date_and_rain in date_and_rain_data:
        if date_and_rain['Rain'] == most_rain:
            rainiest_days.append(date_and_rain['Date'])
    return most_rain, rainiest_days
most_rain, rainiest_days = rainiest_days(date_and_rain_data)
print(f"The rainiest day(s) was/were {rainiest_days} with {most_rain*0.01} in")#maybe wanna pretty this up later

#function to convert to datetime
def get_date_time(date_and_rain_data):
    # datetime_list = []
    for date_and_rain in date_and_rain_data:
        date = datetime.datetime.strptime(date_and_rain['Date'], '%d-%b-%Y')
        date_and_rain['Date'] = (date.year, date.month, date.day)
    return date_and_rain_data
datetime_and_rain_data = get_date_time(date_and_rain_data)
print(datetime_and_rain_data)

#find the year which had the most rain on average
def highest_annual_average_rainfall(datetime_and_rain_data):
    last_year = 0
    year_totals = []
    for datetime_and_rain in datetime_and_rain_data:
        year = datetime_and_rain['Date'][0]

        if year == last_year:
            try:
                year_dict['Total'] += int(datetime_and_rain['Rain'])
            except:
                continue
            
        else:
            try:
                year_totals.append(year_dict)
            except:
                pass
            year_dict = {}
            year_dict['Year'] = datetime_and_rain['Date'][0]
            year_dict['Total'] = 0
            try:
                year_dict['Total'] = int(datetime_and_rain['Rain'])
            except:
                pass
            last_year = year

    most_rain = 0
    for year in year_totals:
        if year['Total'] > most_rain:
            rainiest_year = year['Year']
            most_rain = year['Total']
    # print(f"Rainiest Year: {rainiest_year}")

    rainiest_year_data_for_mean = []
    for datetime_and_rain in datetime_and_rain_data:
        if datetime_and_rain['Date'][0] == rainiest_year:
            rainiest_year_data_for_mean.append(datetime_and_rain)
    # print(rainiest_year_data_for_mean)
    rainiest_year_mean = find_mean(rainiest_year_data_for_mean)
    return rainiest_year, rainiest_year_mean
rainiest_year, rainiest_year_mean = highest_annual_average_rainfall(datetime_and_rain_data)
print(f"{rainiest_year} had the most rainfall on average with {rainiest_year_mean*0.01} in")
