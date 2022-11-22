"""This program is to calculate the age of a person"""

def age(year_birth,current=2022):
    age1 = current-year_birth
    return age1
year = int(input("What is your year of birth "))
print(age(year))
age2 = age(year)
if age2>120:
    print("You are too old")
else:
    print("Hehe How You doin lol ")