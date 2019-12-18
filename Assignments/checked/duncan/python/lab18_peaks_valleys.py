
data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]

def peaks(peak):
    for peak in range(len(data)-1):
        if data[peak] > data[peak-1] and data[peak] > data[peak+1]:
            print(data[peak], end = " ")

def valleys(valley):
    for valley in range(len(data)-1):
        if valley > 0 < len(data)-1:
            if data[valley] < data[valley-1] and data[valley] < data[valley+1]:
                print(data[valley], end = " ")

peaks(data)
print()
valleys(data)
print()

for i in range(len(data)):
    x = "x" * int(data[i])
    print(x)
