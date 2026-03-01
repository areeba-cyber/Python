# Dictionaries are in the key:value format and in curly braces{dict}
chai_types = {"Masala" : "spicy", "Green" : "zesty"}

# How to access individual value
chai_types["Masala"]
chai_types.get("Green")

# How to change values
chai_types["Masala"] = "Fresh"

# For loop
for chai in chai_types:
    print(chai)
    # when we use for loop in dictionaries it will give us keys  and when we use for loop in lists it will give us values 

# To print keys and values both
for chai in chai_types:
    print(chai, chai_types[chai])

    for key, value in chai_types.items():
        print(key, value)

# If condition
if "Masala" in chai_types:
    print("I have masala chai")

# Length
print(len(chai_types))

# POP
chai_types.pop("Masala")
        