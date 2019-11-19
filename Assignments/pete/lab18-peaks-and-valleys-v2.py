'''
lab18-peaks-and-valleys-v2.py
Version2:
Using the data draw the image of x's from the website: https://github.com/PdxCodeGuild/2019-10-28-fullstack-night/blob/master/1%20Python/labs/lab18-peaks_and_valleys.md
'''

data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
count = max(data)
while count != 0:
    for datum in data:
        if datum >= count:
            print(" X ", end='')
        else:
            print("   ", end='')
    print()
    count -= 1
print(data)

