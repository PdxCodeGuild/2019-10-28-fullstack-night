import random

NUMBER_OF_PICKS = 6
MIN_PICK = 1
MAX_PICK = 10
WINNINGS = 100
OFFSETT = 4


def checker(userNums, winningNums):
    if userNums == winningNums:
        print ("\nCongratulations! You Win ${}!".format(WINNINGS),
               "\nYour numbers: ", userNums,
               "\nThe winning lottery numbers were: ", winningNums, "\n")
    else:

        print ("\nSorry, you lose...",
               "\nYour numbers: ", userNums,
               "\nThe winning lottery numbers were: ", winningNums, "\n")


   
def get_user_nums():
    userNums = []
    while len(userNums) < NUMBER_OF_PICKS:
        nums = input("Pick a number {} through {}: ".format(MIN_PICK, MAX_PICK))
        try:
            nums = int(nums)
        except:
            print("Sorry your input must be an integer!")
            continue
        if MIN_PICK <= nums <= MAX_PICK:
            if nums not in userNums:
                userNums.append(nums)
            else:
                print("Error! You have already picked this number")
        else:
            print("Error! Your number was not in range")

    return sorted(userNums)


def get_winning_nums():
    return sorted(random.sample(range(MIN_PICK, MAX_PICK), NUMBER_OF_PICKS)) 



def lottery_menu():
    name = ' '*int(OFFSETT/2) + "LOTTERY MENU"
    dotted = (OFFSETT+len(name))*'-'
    options = ["[Play Pick {}]".format(NUMBER_OF_PICKS), 
               "[Exit]"]
    print('{} \n{} \n{}'.format(dotted, name, dotted))
    for i, opt in enumerate(options):
        print(i+1, opt)
    print(dotted)


def play_pick_n():
    userNums = get_user_nums()
    winningNums = get_winning_nums() 
    checker(userNums, winningNums)



def main():
    lottery_menu()
    while True:
        choice = input("\nEnter your choice[1-2]: ")
        if choice == '1':
            string = "\n[Play Pick {}]".format(NUMBER_OF_PICKS) + "selected!"
            dotted = '\n'+ len(string) * "-"

            print(dotted,
                  string,
                  dotted)

            play_pick_n()
            break

        elif choice == '2':
            print ("Thanks for playing!\n")
            break

        print("Error! Invalid input. Press any key to continue...\n")

if __name__ == '__main__':
    main()

