# Python Lists
# 1.Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,
exp = [2200, 2350, 2600, 2130, 2190]
# 1. In Feb, how many dollars you spent extra compare to January?
print("In feb I spent ",exp[1]-exp[0],"extra expenses" )

# 2. Find out your total expense in first quarter (first three months) of the year.
print("The total expense in first quater is:", exp[0]+exp[1]+exp[2])

# 3. Find out if you spent exactly 2000 dollars in any month
print("Did I spent 2000$ in any month?", 2000 in exp)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
print(exp + [1980])

exp.append(1980)
print("The expenses at the end of june is:", exp)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
exp[3] = exp[3] - 200
print("Expenses after 200$ return in April:",exp)


# 2.You have a list of your favourite marvel super heros.
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this find out,
heros=['spider man','thor','hulk','iron man','captain america']
# 1. Length of the list
print(len(heros))

# 2. Add 'black panther' at the end of this list
heros.append('black panther')
print(heros)

# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)

# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
heros[1:3]=['doctor strange']
print(heros)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heros.sort()
print(heros)


#  Python If Condition
# 1. Using following list of cities per country,
# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"]
# Write a program that asks user to enter a city name and it should tell which country the city belongs to
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = input("Enter city name:")

if city in india:
    print(f"The {city} is in India")
elif city in pakistan:
    print(f"The {city} is in Pakistan")
elif city in bangladesh:
    print(f"The {city} is in Bangladesh")
else:
    print(f"I won't be able to tell you which country {city} is in! Sorry!")   

# Write a program that asks user to enter two cities and it tells you if they both are in same country or not. For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print "They don't belong to same country"

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter city 1:")
city2 = input("Enter city 2:")

if city1 in india and city2 in india:
    print(f"{city1} and {city2} are in india")
elif city1 in pakistan and city2 in pakistan:
    print(f"{city1} and {city2} in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print(f"{city1} and {city2} are in bangladesh")
else:
    print(f"{city1} and {city2} are not in same country")              

# 2. Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
# Ask user to enter his fasting sugar level
# If it is below 80 to 100 range then print that sugar is low
# If it is above 100 then print that it is high otherwise print that it is normal

sugar=input("Please enter your fasting sugar level:")
sugar=float(sugar)
if sugar<80:
    print("Your sugar is low, go eat some jalebi :)")
elif sugar>100:
    print("Your sugar is high, stop eating all mithais..!")
else:
    print("Your sugar is normal, relax and enjoy your life!")