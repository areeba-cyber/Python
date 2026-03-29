# Python for loop

# 1. After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads

result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for item in result:
    if item == "heads":
        count += 1
print("Heads count: ",count)

# 2.Print square of all numbers between 1 to 10 except even numbers
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i*i)

# 3.Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

month_list = ["January", "February", "March", "April", "May"]
expense_list = [2340, 2500, 2100, 3100, 2980]
e = input("Enter expense amount: ")
e = int(e)

month = -1
for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break

if month != -1:
    print(f'You spent {e} in {month_list[month]}')
else:
    print(f'You didn\'t spend {e} in any month')

# 4.Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message
for i in range(5):
    print(f"You ran {i+1} miles") # i starts with zero hence adding 1
    tired = input("Are you tired? ")
    if tired == 'yes':
        break

if i == 4: # 4 because the index starts from 0
    print("Hurray! You are a rock star! You just finished 5 km race!")
else:
    print("You didn't finish 5 km race but hey congrats anyways! You still ran {i+1} miles")

# 5.Write a program that prints following shape

# *
# **
# ***
# ****
# *****
for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)

# Functions in python
# 1.Write a function called calculate_area that takes base and height as an input and returns and area of a triangle. Equation of an area of a triangle is,
# area = (1/2)*base*height

def calculate_area(base, height):
    area = (1/2)*base*height
    return area
result = calculate_area(10,5)
print(result)

# 2.Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area. Equation of rectangle's area is,
# rectangle area=length*width
# If no shape is supplied then it should take triangle as a default shape

def calculate_area(base, height, shape="triangle"):
    if shape=="triangle":
        area=1/2*(base*height) # Triangle area is : 1/2(Base*Height)
    elif shape=="rectangle":
        area=base*height # Rectangle area is: Length*Width
    else:
        print("Error: Input shape is neither triangle nor rectangle.")
        area=None # If user didn't supply "triangle" or "rectangle" as shape then return None
    return area

# 3.Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# *
# **
# ***
# if input is 4 then it should print

# *
# **
# ***
# ****
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def print_pattern(n):
    for i in range(1, n + 1):        # controls number of lines
        for j in range(i):           # prints stars in each line
            print("*", end="")
        print()                      # move to next line

#   print_pattern(3)
# print_pattern(4)      