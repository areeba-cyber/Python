# Used to enhace the code, write the code in best possible way,
# Increase performance, decrease the size of code

marks = [10,20,30,40,50]
new_marks = []
for x in marks:
    new_marks.append(x+2)
print(new_marks)

# List Comprehension
marks = [10,20,30,40,50]
new_marks = [x+2 for x in marks]
print(new_marks)