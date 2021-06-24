
'''
#global
name='this is global string'
def greet():
    name='i am enclosing'
    def hello():
        #local
        name='i am local'
        print('hello'+ 'name')
    hello()

'''
float='it is a float'
def percentage():
    name='college'
    def hello():
        name='student'
        print('hello'+'name')
    hello() 
