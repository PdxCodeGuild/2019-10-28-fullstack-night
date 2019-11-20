# rain_data_file = 'nw_portland_rain_data.txt'
def read_rain_data(rain_data_file):
    with open(rain_data_file) as rain_data_raw:
        lines = rain_data_raw.readlines()

    rows = []
    for line in lines:
        row = line.strip()
        rows.append(row)
    # print(rows)
    count = 0
    for row in rows:
        rows.pop(count)
        # print(pop_row)
        if row == '-' * len(row):
            break
        count += 1
    rows = rows[count:]

    print(rows[::-1])
    date_and_rain_data = []
    for row in rows:
        date_and_rain = {}
        columns = row.split()
        try:
            date_and_rain[columns[0]] = int(columns[1])
        except:
            date_and_rain[columns[0]] = columns[1]
            print(date_and_rain)
        # date_and_rain = dict(zip(columns[0], columns[1]))
        date_and_rain_data.append(date_and_rain)
    return date_and_rain_data
read_rain_data('nw_portland_rain_data.txt')
result = read_rain_data('nw_portland_rain_data.txt')
# print(result[::-1])