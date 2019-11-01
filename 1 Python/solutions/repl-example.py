# Running state
running = True

# While it's running
# LOOP
while running:
  # READ
  value = input("Enter anything or done to exit: ")
  # EVALUATE
  if value == "done":
    running = False
    break
  # PRINT
  print(value)

