data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

# for x, datum in enumerate(data):
#     for y in range(highest_peak):

height = max(data)
width = len(data)
starting_tuple = (0, height)

counter_dict = {
    'X_count': 0,
    "O_count": 0,
    "_count":  0,
}

def iterate_over(data, width, height, xy_tuple, counter_dict, count=1):
    # print(count)
    count +=1
    x = xy_tuple[0]
    y = xy_tuple[1]
    datum = data[x]

    if y <= 0:
        return(counter_dict)

    if y <= datum:
        print(' X ', end='')
        counter_dict['X_count'] += 1
    elif data[x:] and data[:x]:
            if y <= max(data[x:]) and y <= max(data[:x]):
                print(' O ', end='')
                counter_dict['O_count'] += 1
            else:
                print('   ', end='')
                counter_dict['_count'] += 1
    else:
        print('   ', end='')
        counter_dict['_count'] += 1

    if x < width - 1:
        iterate_over(data, width, height, (x + 1, y), counter_dict, count)
    else:
        print()
        iterate_over(data, width, height, (0, y - 1), counter_dict, count)

iterate_over(data, width, height, starting_tuple, counter_dict)
print(counter_dict)