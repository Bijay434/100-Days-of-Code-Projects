"""
If the bill was $150.00, split between 5 people, with 12% tip.
Each person should pay (150.00 / 5) * 1.12 = 33.6
Format the result to 2 decimal places = 33.60
"""
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

print("Welcome to the tip calculator!")
bill_amount = float(input("What was the total bill amount? $"))
tip = float(input("How much do you want to tip? 10, 12, 15, or 20? "))
person = float(input("How many people are there to split the bill? "))

bill_per_person = (bill_amount / person) * (1 + tip / 100)
final_bill = "{:.2f}".format(bill_per_person, 2)

print(f"Each person should pay ${final_bill}.")
