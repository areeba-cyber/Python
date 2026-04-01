List = [1,2,3,4,5,6]
It = iter(List)
while True:
    try:
     print(next(It))
    except Exception as e:
       break