word1 = input('enter a word')

test = word1[::-1]

while True: 
    if word1 == test:       
        print ('true')
    else:
        print("False")
    break
