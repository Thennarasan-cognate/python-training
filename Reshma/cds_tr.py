score=5
b=67
def a():
       
        #globals()['Age']=27
        score=10
        print("age3 is : ",b)
        print("age4 is : ",score)
        print
        print("age5 is : ",globals()['score'])
        return
print("age1 outside the function: ",score)
a()
print("age2 outside the function: ",score)
