#global
name='this is a global string'
def greet():
    
#enclosing
    name='I am enclosing'
    def hello():
        #local
        #name='I am local'
        print('hello' + name)
    hello()
keertipati anand kumar11:31 AM
float='it is a float'
def percentage():
    name='college'
    def hello():
        name='student'
        print('hello'+'name')
hello()   
keertipati anand kumar11:33 AM
float='it is a float'
def percentage():
    name='college'
    def hello():
        name='student'
        print('hello'+'name')
    hello()   
R Ramya11:33 AM
name='Ramya'
def keerthi():
    name='I am keerthi'
    def reshma():
        name='I am Reshma'
        print('hello' + name)
    reshma()
reshma samy11:38 AM
#global
bookcost=24.95
numbook=60.0
def cost():
#enclosing
    bookcost= 'i am enclosing'
    def book():
    #local
    #bookcost='25.95'
    print('bookcost'+numbook)
    bookcost()
bookcost()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    bookcost()
TypeError: 'float' object is not callable
>>> 
keertipati anand kumar11:39 AM
a='it is a value'
def percentage():
    name='college'
    def hello():
        name='student'
        print('hello'+'name')
    hello()   
You11:46 AM
#global
bookcost=24.95
numbook=60.0
def cost():
#enclosing
    #bookcost= 'i am enclosing'
    def book():
    #local
    #bookcost='25.95'
            print('bookcost '+ str(numbook))
    book()
You11:53 AM
.
import reshma
reshma.cost()
keertipati anand kumar12:04 PM
 import os
>>> os.getcwd()
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python39'
R Ramya12:04 PM
>>> import os
>>> os.getcwd()
'C:\\Users\\Ramya\\AppData\\Local\\Programs\\Python\\Python39'
You12:05 PM
>>> import os
>>> os.mkdir("c:\\hello_team")
>>> os.mkdir("c:\\COGNATE")
>>> os.mkdir("C:\\Users\\User\\Desktop\\hello_team")
>>> os.getcwd()
'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python39'
reshma samy12:07 PM
import os
>>> os.getcwd()
'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python39'
>>>
You12:10 PM
>>> os.chdir("c:\\hello_team")
>>> os.getcwd()
'c:\\hello_team'
change the current working directory location to the directory location of my choice
You12:13 PM
.
>>> os.listdir("c:\\COGNATE")
['anand', 'ramya', 'reshma']
You12:15 PM
.
>>> os.rmdir("c:\\COGNATE")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    os.rmdir("c:\\COGNATE")
OSError: [WinError 145] The directory is not empty: 'c:\\COGNATE'
>>> os.rmdir("c:\\COGNATE")
R Ramya12:16 PM
is there  any option to remove the folder inside of cognate dir using command
You12:17 PM
os.rmdir("c:\\COGNATE\\ramya")
You12:19 PM
.
>>> import random
>>> random.random()
0.37373696672904855
>>> random.random()
0.4693121139501816
>>> random.random()
0.9979831050423845
>>> random.random()
0.7180729413124461
You12:21 PM
.
>>> random.randint(1,7)
6
>>> random.randint(1,7)
4
>>> random.randint(1,7)
6
>>> random.randint(1,7)
4
>>> random.randint(1,7)
3
>>> random.randint(1,7)
7
>>> random.randint(1,7)
4
You12:24 PM
.
>>> random.randrange(1,10,2)
7
>>> random.randrange(1,10,2)
1
>>> random.randrange(1,10,2)
5
>>> random.randrange(1,10,2)
5
>>> random.randrange(1,10,2)
5
>>> random.randrange(1,10,2)
7
>>> random.randrange(1,10,2)
3
>>> random.randrange(1,10,2)
7
>>> random.randrange(1,10,2)
1
>>> random.randrange(1,10,2)
9
You12:27 PM
.
>>> random.choice(('anand','ramya','reshma','thenna',66,9.2))
'reshma'
>>> random.choice(('anand','ramya','reshma','thenna',66,9.2))
'anand'
>>> random.choice(('anand','ramya','reshma','thenna',66,9.2))
66
>>> random.choice(('anand','ramya','reshma','thenna',66,9.2))
9.2
>>> random.choice(('anand','ramya','reshma','thenna',66,9.2))
66
>>> random.choice(('anand','ramya','reshma','thenna',66,9.2))
66
>>> random.choice(('anand','ramya','reshma','thenna',66,9.2))
'ramya'
You12:29 PM
.
>>> mem=['anand','ramya','reshma','thenna',66,9.2]
>>> random.shuffle(mem)
>>> mem
[66, 'reshma', 'anand', 'ramya', 9.2, 'thenna']
You12:33 PM
>>> import math
>>> math.sqrt(4)
2.0
>>> math.sqrt(25)
5.0
You12:35 PM
>>> math.pow(2,5)
32.0
>>> 2**5
32
>>> math.log(34)
3.5263605246161616
>>> math.log(50)
3.912023005428146
You12:37 PM
Using Logarithmic Functions
Much of the power of logarithms is their usefulness in solving exponential equations. Some examples of this include sound (decibel measures), earthquakes (Richter scale), the brightness of stars, and chemistry (pH balance, a measure of acidity and alkalinity).
>>> math.log(34)
3.5263605246161616
>>> math.log(50)
3.912023005428146
>>> math.log10(34)
1.5314789170422551
>>> math.log10(50)
1.6989700043360187
You12:40 PM
.
>>> math.exp(5)
148.4131591025766
>>> math.e
2.718281828459045
>>> 2.7**5
143.48907000000005
>>> 2.718281828459045**5
148.41315910257657
i,e 2 to the power of 5
You12:41 PM
.
>>> math.ceil(5.986)
6
>>> math.floor(5.986)
5
>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
You12:42 PM
22/7
You12:47 PM
.
>>> import math
>>> math.radians(180)
3.141592653589793
>>> math.degrees(math.pi)
180.0
>>> 
>>> math.tan(math.radians(30))
0.5773502691896257
>>> math.sin(math.radians(90))
1.0
>>> math.cos(math.radians(30))
0.8660254037844387
