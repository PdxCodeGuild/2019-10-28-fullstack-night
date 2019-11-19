def validator(n):

    validatelist=[]

    for i in n:
        validatelist.append(int(i))


    for i in range(0,len(n),2):


        validatelist[i] = validatelist[i]*2

        if validatelist[i] >= 10:

            validatelist[i] = validatelist[i]//10 + validatelist[i]%10


    if sum(validatelist)%10 == 0:
        print('This a valid credit card') 

    else:
        print('This is not valid credit card')

def cardnumber():

    result=''
    while True:
        try:
            result = input('Please enter the 16 digit credit card number : ')

            if not (len(result) == 16) or not type(int(result) == int) :
                raise Exception

        except Exception:    
            print('That is not a proper credit card number. \nMake sure you are entering digits not characters and all the 16 digits.')
            continue

        else:
            break


    return result

def goagain():
    return input('Do you want to check again? (Yes/No) : ').lower()[0] == 'y'

def main():

    while True:

        result = cardnumber()
        validator(result)


        if not goagain():
            break

if __name__ == '__main__':
    main()


