# Crearting a love calculator using python.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name_concat = name1.lower()+name2.lower()
true = name_concat.count('t') + name_concat.count('r') + name_concat.count('u')+name_concat.count('e')
love = name_concat.count('l') + name_concat.count('o') + name_concat.count('v')+name_concat.count('e')
love_score = int(str(true) + str(love))
if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <=50:
    print(f"Your love score is {love_score}, you are fine together.")
else:
    print(f"Your love score is {love_score}.")
