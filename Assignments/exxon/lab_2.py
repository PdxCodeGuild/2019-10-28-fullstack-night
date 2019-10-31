
print(" welcome to the Madlib program")

# 'if you can dodge a ball, you can dodge a wrench!'



def verb():
    v = input(' give me a transition verb: ')
    return v

def noun1():
    n = input ("give me a noun:")
    return n

def noun2():
    n2 = input ("give me another noun:")
    return n2



def main():

    v = verb()
    n = noun1()
    n2 = noun2()

    print(f"if you can {v} a {n}, you can {v} a {n2}!")

main()