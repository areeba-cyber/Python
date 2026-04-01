import sys  
# sys is system
def creater():
    list=[]
    i=1
    while i<=200:
        list.append()
        i += 1 
        return list
    
print (creater )
z= sys.getziseof(list)
print(z)
print([num+10 for num in creater()])
# It occupy huge space 

# In generator we are using the memory in one time instead using it i an efficient way 
def creator():
    i = 1
    while i<=200:
        yield i
        i += 1
# It will create a memory
print (creator())
#It will print one by one 
x = creator()
print(next(x))   
print(next(x))   
# It will print all list
print(list(x))

