'''
lab18-peaks-and-valleys-v3.py

Version3
Imagine pouring water into onto these hills. The water would wash off the left and right sides, but would accumulate in the valleys. Below the water is represented by O's. Given data, calculate the amount of water that would be collected.

                                                  X  O  O  O  O  O  X
                                               X  X  X  O  O  O  X  X
                          X  O  O  O  O  O  X  X  X  X  X  O  X  X  X
                       X  X  X  O  O  O  X  X  X  X  X  X  X  X  X  X
                    X  X  X  X  X  O  X  X  X  X  X  X  X  X  X  X  X
                 X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
              X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
           X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
        X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
'''
#indices1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19 20 21
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

#this function finds the highest number in the data
def max_finder(data):
    return max(data)


#this function reverses the data list
def backwardser(data):
    return data[::-1]

#this function counts the valley fillers
def valley_filler(data):
    count = 0
    O_count = 0
    first_run = True
    for datum in data:
        count += 1
        if datum < max_finder(data):
            O_count += max_finder(data) - datum
        if first_run != True and datum == max_finder(data):
            break
        first_run = False
    return (O_count, count)

#this pops the used indices from the list
def data_truncator(data):
    pop_num = valley_filler(data)[1]
    data = backwardser(data)
    for i in range(pop_num):
        data.pop()
    data = backwardser(data)
    return data

#this puts the valley fill counts together
# def valley_fill_combiner(data):
#     while len(data) != 0:
#         valley_filler(data)
#         data_truncator(data)
#     return
        
data = backwardser(data)



print("First run:")
print(f"max_finder(data) = {max_finder(data)}")
print(f"valley_filler(data) = {valley_filler(data)}--O_count, count")
print(f"data_truncator(data) = {data_truncator(data)} length = {len(data_truncator(data))}")
print(f"backwardser(data) = {backwardser(data)}")
print()

first_result_valley_filler = valley_filler(data)
first_result_data_truncator = data_truncator(data)
print("Second run:")
print(f"valley_filler(data_truncator(data)) = {valley_filler(data_truncator(data))}")