nums = [5, 0, 8, 3, 4, 1, 6]

# # loop over the elements
# for x in nums:
#     print(x)
#
# # loop over the indices
# for i in range(len(nums)):
#     print(nums[i])
#
# nums.append(5)
# print(nums)

game_in_session = "yes"

while game_in_session == "yes":
    game_in_session = input("Do you want to append a number? ").lower()
    if game_in_session == "yes":
        user_choice = input("What number do you want to append or say done? ")
        if type(user_choice) == int:
            nums.append(user_choice)
            game_in_session = "yes"
            print(nums)
            print(f"Average: {(sum(nums) / len(nums))}.")
        elif user_choice == "done": # superficial b/c "user_choice" is an interger
            game_in_session = "no"
            print(nums)
            print(len(nums))
else:
    print("Goodbye!")
