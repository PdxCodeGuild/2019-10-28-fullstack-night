'''
Lab 02: mad-libs.py
Make a mad libs program.
'''
print("Welcome to Mad Libs")
while True:
    # Ver 2: utilize lists with split()
    person = input(
        "\nPlease enter 2 different types of people, separated by commas: ").split(',')
    person1 = person[0]
    person2 = person[1]

    place = input(
        "Please enter 4 different places, separated by commas: ").split(',')
    place1 = place[0]
    place2 = place[1]
    place3 = place[2]
    place4 = place[3]

    job1 = input("Please enter a job: ")

    adjective = input(
        "Please enter 7 adjectives, separated by commas: ").split(',')
    adjective1 = adjective[0]
    adjective2 = adjective[1]
    adjective3 = adjective[2]
    adjective4 = adjective[3]
    adjective5 = adjective[4]
    adjective6 = adjective[5]
    adjective7 = adjective[6]

    verb = input("Please enter 5 verbs, separated by commas: ").split(',')
    verb1 = verb[0]
    verb2 = verb[1]
    verb3 = verb[2]
    verb4 = verb[3]
    verb5 = verb[4]

    thing = input("Please enter 4 things, separated by commas: ").split(',')
    thing1 = thing[0]
    thing2 = thing[1]
    thing3 = thing[2]
    thing4 = thing[3]

    food = input("Please enter 2 types of food, separated by a comma: ").split(',')
    food1 = food[0]
    food2 = food[1]

    drink = input(
        "Please enter 2 types of drink, separated by a comma: ").split(',')
    drink1 = drink[0]
    drink2 = drink[1]

    while True:
        print(f"\nThere once was a {person1} who lived in a {place1}.  The {person1} worked as a {job1} at the town {place2}.  One day the {person1}'s boss, who was {adjective1}, made the {person1} {verb1} the {thing1}, without pay.  This made the {person1} feel really {adjective2}, so after work the {person1} met a friend who was a {person2} at their favorite {place3}.  They ate {food1} and drank {drink1} until they felt {adjective3} and the {person1} told the {person2} that they wanted to {verb2} their boss with a {thing2} in the {place4}.  So they went to the boss's house in the {adjective4} part of town and {verb3}ed the boss with a {thing3} until the boss looked pretty {adjective5}.  The boss said, \"You two have made me feel very {adjective6} and I've decided to drink {drink2} and eat {food2} with you both until we're all {adjective7}.\"  So the boss did just that until {person1} and {person2} {verb4}ed and they went to {person1}'s {place1} and {verb5}ed on the {thing4} until the sun came up.\n\n~Fin~")
        hear_again = input("\nWould you like to hear your story again? ")
        if hear_again in ['yes', 'ye', 'yeah', 'y', 'sure', 'why not']:
            continue
        else:
            break

    another_story = input("\nWould you like to make a new story? ")
    if another_story in ['yes', 'ye', 'yeah', 'y', 'sure', 'why not']:
        continue
    else:
        break
print("\nThanks for playing Mad Libs!")
