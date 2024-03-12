unit = input("Do you want to enter your weight in KG or LB? ").upper()
weight = float(input("What is your weight? "))
if unit == "KG":
    print(f"Your weight is {weight * 2.2} LB")
elif unit == "LB":
    print(f"Your weight is {weight * 0.453} KG")
else:
    print("Please either type KG or LB")
