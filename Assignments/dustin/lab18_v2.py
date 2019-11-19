'''
By: Dustin DeShane
Filename: lab18.py
'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
count = max(data)
for i in data:
    print("\n")
    for j in data:
        if j >= count:
            print("X", end='  ')
        else:
            print(" ", end='  ')
        #print(data)
        #print(count)
    if count == 1:
        break
    count -= 1
print("\n")
print("  ".join( str(e) for e in data ))