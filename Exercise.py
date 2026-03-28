# Exercise: Python Variables
# 1. Create a variable called break and assign it a value 5. See what happens and find out the reason behind the behavior that you see.

# break = 5
# Break is a reserved keyword (used in for and while loop to exit a loop) in python not a variable name Thats why it is showing error

# 2. Create two variables. One to store your birth year and another one to store current year. Now calculate your age using these two variables

X = 2003
Y = 2026
age = Y - X
print("My age is: ", age)


# 3. Store your first, middle and last name in three different variables and then print your full name using these variables

First = "Areeba"
Middle = "Khalid"
Last = "Rajpoot"
print("My name is: " +First+ " " +Middle+ " " + Last)

# 4. Answer which of these are invalid variable names: _nation 1record record1 record_one record-one record^one continue
# 1record, record-one, record^one, continue

# Numbers in python
# 1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total area using python and print it.

L = 92
w = 48.8
Area = L * w
print("Area is :", Area)

# 2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?

num_packets = 9
cost_per_packet = 1.49
total_cost = num_packets*cost_per_packet
money_paid = 20
money_back = money_paid - total_cost
print("Cash back:", money_back)

# 3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet is its length. If tiles cost 500 rs per square feet, how much will be the total cost to replace all tiles. Calculate and print the cost using python (Hint: Use power operator ** to find area of a square)

length=5.5
area=length**2 # area of square is length power 2
cost=area*500
print("total cost for bathroom tiles replacement:",cost)

# 4. Print binary representation of number 17
num=17
print('Binary of number 17 is:',format(num,'b'))


# String in Python
# 1. Create 3 variables to store street, city and country, now create address variable to store entire address. Use two ways of creating this variable, one using + operator and the other using f-string. Now Print the address in such a way that the street, city and country prints in a separate line

Street = "Street NO 3"
City = "Okara"
Country = "Pakistan"
address1 = Street + '\n' + City + '\n' + Country
print("Address in + format is :", address1)
address2 = f'{Street}\n{City}\n{Country}'
print("Address in f format is:",  address2)

# 2. Create a variable to store the string "Earth revolves around the sun"
# Print "revolves" using slice operator
# Print "sun" using negative index
# 3. Create two variables to store how many fruits and vegetables you eat in a day. Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables and fruits that you eat everyday. Use python f string for this.
# 4. I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong with new ones and print the new string. Also try to do this in one line.