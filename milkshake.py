balance = float(input("Enter your budget: "))
shakes = {1: 4.00, 2: 4.25, 3: 4.50, 4: 5.00}
while True:
  choice = int(
      input(
          "Enter your choice:\n1. Vanilla\n2. Chocolate\n3. Strawberry \n4. Mango\n5. Quit "))
  
  if choice == 1:
    if balance >= shakes[1]:
      balance -= shakes[1]
      print("Enjoy your Vanilla milkshake, your new balance is ", balance)
    else:
      print("You're broke, go home")
  elif choice == 2:
    if balance >= shakes[2]:
      balance -= shakes[2]
      print("Enjoy your Chocolate milkshake, your new balance is", balance)
    else:
      print("You're broke, go home")
  elif choice == 3:
    if balance >= shakes[3]:
      balance -= shakes[3]
      print("Enjoy your Strawberry milkshake, your new balance is", balance)
    else:
      print("You're broke, go home")

  elif choice == 4:
    if balance >= shakes[4]:
      balance -= shakes[4]
      print("Enjoy your Mango milkshake, your new balance is", balance)
    else:
      print("You're broke, go home")
  elif choice == 5:
    break
  else:
    print("Invalid Input. Please enter a number between 1 and 5")
