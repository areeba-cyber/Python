In Python, numbers are data types used to store numeric values like integers, decimals, and complex numbers.

Python mainly has 3 types of numbers:
1️⃣ Integers (int)
2️⃣ Floating Point Numbers (float)
3️⃣ Complex Numbers (complex)

x=2
y=3
z=4
x+y
40 + 20.23 = 60.23 
# This is correct but it is better to keep the data types same
float(40) + 20.23
40 + int(20.23)

OPERATOR OVERLOADING 
'Areeba' + 'KHALID'
# The plus sign will automatically look at left and right and if the datatype is same then it concatenate the lest side and right side (This is operator overloading and seems in every language)

2**10 (2 ki power 10 = 200)

repr('areeba') (result= "'areeba'")
str('areeba') (result= 'areeba')
print('areeba') (result= areeba)

# Booleans are also treated as numbers in python
2>1 (result= True) 
4.0 != 5.0 (result= True)
x<y<z
x<y and y<z