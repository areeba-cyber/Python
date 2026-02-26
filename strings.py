chai = "Lemon Chai"
print(chai)
# and if we are on terminal(shell) then we also write simply chai instead of print and it will dive the value that we are storing in chai

# To print first character
chai = "Lemon chai"
first_char = chai[0]
print(first_char)

# Slice
chai = "Lemon Chai"
slice_chai = chai[0:5]
print(slice_chai)

# Upper and Lower case
print(chai.lower())
print(chai.upper())

# To remove extra spaces
print(chai.strip())

# Replace
chai = "Lemon chai"
print(chai.replace("Lemon", "Ginger"))

# To convert string into list
chai = "Lemon, Ginger, Tea, Cup"
print(chai.split(", "))

# Find
chai = "Lemon chai"
print(chai.find("chai"))

# Count
chai = "Lemon chai chai ginger chai"
print(chai.count("chai"))

# Format
cahi_type = "Masala"
quantity = 2
order = " I ordered {} of {} chai "
print(order.format(quantity, chai_type))

# Join
chai_variety = ["Lemon", "Masala", "Ginger"]
print(" ".join(chai_variety))
print(len(chai))

chai = "He said" , \"Masala chai is awesome\" "


# Raw string
chai = r"Masala\nChai"