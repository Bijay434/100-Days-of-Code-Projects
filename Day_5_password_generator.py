# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password_list = [letters, numbers, symbols]
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for char in range(0, nr_letters):
    password += random.choice(letters)
for numb in range(0, nr_numbers):
    password += random.choice(numbers)
for symb in range(0, nr_symbols):
    password += random.choice(symbols)
print(f"Password: {password}")


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password01 = []
for char in range(0, nr_letters):
    password01.append(random.choice(letters))
for numb in range(0, nr_numbers):
    password01.append(random.choice(numbers))
for symb in range(0, nr_symbols):
    password01.append(random.choice(symbols))
hard_password = ""
random.shuffle(password01)
for char in password01:
    hard_password += char
print(f"Hard Password: {hard_password}")


"""
password_length = nr_symbols+nr_numbers+nr_letters
for pass_word in range(0,password_length):
    password01 += random.choice(random.choices(password_list, weights=map(len, password_list))[0])
print(f"Hard Password: {password01}")
"""