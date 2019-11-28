
### PALINDROME ###

def check_palindrome(user_palindrome):
    # user_palindrome = input("Enter word for palindrome check: ")
    if user_palindrome == user_palindrome[::-1]:
        print(f"Yes {user_palindrome} is a palindrome of {(user_palindrome)[::1]}!")
    elif user_palindrome != user_palindrome[::-1]:
        print(f"No, {(user_palindrome)[::1]} is not a palindrome of {user_palindrome}.")
    else:
        print("Error")

check_palindrome("racecar")
check_palindrome("palindrome")

### ANAGRAM ###

def check_anagram(user_anagram1, user_anagram2):
    user_anagram1a = user_anagram1.lower().replace(" ", "")
    user_anagram1a = sorted(user_anagram1a)

    user_anagram2a = user_anagram2.lower().replace(" ", "")
    user_anagram2a = sorted(user_anagram2a)

    if user_anagram1a == user_anagram2a:
        print(f"Yes {user_anagram1} is an anagram of {user_anagram2}.")
    elif user_anagram1a != user_anagram2a:
        print(f"No, {user_anagram1} and {user_anagram2} are not anagrams.")

check_anagram("anagram", "nag a ram")
check_anagram("duncan", "duncant")
