score=7
b=67
def a():
     globals()['b']=27
     Age=12
     print("age3 is :",b)
     print("age4 is :",Age)
     print("age5 is :",globals()['b'])
     return
print("age2 outside the function:", score)
a()
print("age1 outside the function:", score)
