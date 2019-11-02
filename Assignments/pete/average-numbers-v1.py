'''
average-numbers-v1.py
Lab 10: Average Numbers
We're going to average a list of numbers. Start with the following list, iterate through it, keeping a 'running sum', then divide that sum by the number of elements in that list. Remember len will give you the length of a list.

The code below shows how to loop through an array, and prints the elements one at a time.
'''
nums = [5, 0, 8, 3, 4, 1, 6]

# # loop over the elements
# for num in nums:
#     print(num)

# #loop over the indices
# for i in range(len(nums)):
#     print(nums[i])

running = True
sum_nums = sum(nums)
avg_nums = sum_nums / (len(nums))
print(f"The sum of the list is {sum_nums} so the average is {avg_nums}.")