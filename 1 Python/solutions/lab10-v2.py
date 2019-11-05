numbers = []

# LOOP
while True:
  # READ
  user_input = input("Enter a number or done: ")
  # EVALUATE
  if user_input == "done":
    break
  # PRINT? Actually append to the list
  # CATCH ALL INPUT ERRORS
  try:
    num = float(user_input)
    numbers.append(num)
  except:
    print("Enter a valid number!")
    continue

# Sum our numbers together into the total
total = 0
for num in numbers:
  total += num

avg = total / len(numbers)
# avg = sum(numbers) / len(numbers)

print(f"Your average is {avg}")