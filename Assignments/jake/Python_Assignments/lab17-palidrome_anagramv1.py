def compare(str1,str2):

    if((str1==None) or (str2==None)):

        print(" You don't enter string .")

    elif(len(str1)!=len(str2)):

        print(" Strings entered is not Anagrams .")

    elif(len(str1)==len(str2)):

        b=[]

        c=[]

        for i in str1:

            #print(i)

            b.append(i)

        b.sort()

        print(b)

        for j in str2:

            #print(j)

            c.append(j)

        c.sort()

        print(c)

        if (b==c and b!=[] ):

            print(" String entered is Anagram .")

        else:

            print(" String entered are not Anagram.")

    else:

        print(" String entered is not Anagram .")

str1=input(" Enter the first String :")

str2=input(" Enter the second String :")

compare(str1,str2)