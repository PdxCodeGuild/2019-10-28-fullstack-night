
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
data = list(range(4, 1, -1)) + list(range(1, 4)) # this data shouldn't say that the first index is a peak, but it does say that

def peaks(peak):
    for peak in range(len(data)-1): # this shouldn't start at zero
        if data[peak] > data[peak-1] and data[peak] > data[peak+1]:
            print(data[peak], end = " ")

def valleys(valley):
    for valley in range(len(data)-1):
        if valley > 0 < len(data)-1: # nice, but you should just change the range to range(1, len(data)-1)
            if data[valley] < data[valley-1] and data[valley] < data[valley+1]:
                print(data[valley], end = " ")

'''
In both functions you are creating a parameter, then overwriting it with
the loop variable. Both functions should have one of these lines
for i in range(1, len(peak)):
for i in range(1, len(valley)):
'''
peaks(data)
print()
valleys(data)
print()

for i in range(len(data)):
    x = "x" * int(data[i])
    print(x)
