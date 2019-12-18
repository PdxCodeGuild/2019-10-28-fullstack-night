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
data = [3, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
O_count = 0
count = max(data)
while count != 0:
    for i, datum in enumerate(data):
        if datum >= count:
            print(" X ", end='')
        elif data[:i] and data[i:]:
            if count <= max(data[:i]) and count <= max(data[i:]):
                print(" O ", end='')
                O_count += 1
            else:
                print("   ", end='')
        else:
            print("   ", end='')
    print()
    count -= 1
print(data)
print(O_count)
