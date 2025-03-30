print("Welcome to the tip calculator!")
bill = float(input("What was the total bill?  $"))
tip = float(input("How much tip would you like to give? 10, 12, or 15?  ")) /100 + 1
split = int(input("how many people to split the bill?  "))
print(f"Each person should pay: ${round(bill * tip / split, 2):.2f}")