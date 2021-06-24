Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dct={'reshma':'savadikuppam','ramya':'cuddalore','anand':'railwaykodur','thenna':'sathavattam'}
>>> dct.items()
dict_items([('reshma', 'savadikuppam'), ('ramya', 'cuddalore'), ('anand', 'railwaykodur'), ('thenna', 'sathavattam')])
>>> dct.keys()
dict_keys(['reshma', 'ramya', 'anand', 'thenna'])
>>> dct.values()
dict_values(['savadikuppam', 'cuddalore', 'railwaykodur', 'sathavattam'])
>>> 
>>> 1>2
False
>>> 2>1
True
>>> a=3
>>> type(a)
<class 'int'>
>>> a=True
>>> type(a)
<class 'bool'>
>>> b=None
>>> type(b)
<class 'NoneType'>
>>> st={'chennai','andhar',65,8+4j,'anadhar'}
>>> st{'andhar',65,'chennai',(8+4j)}
SyntaxError: invalid syntax
>>> st
{65, 'chennai', (8+4j), 'andhar', 'anadhar'}
>>> lst=['chennai','andhar',65,8+4j,'anadhar']
>>> lst
['chennai', 'andhar', 65, (8+4j), 'anadhar']
>>> st={'chennai','andhar',65,8+4j,'anadhar',('hi,6.4)}
					  
SyntaxError: EOL while scanning string literal
>>> st={'chennai','andhar',65,8+4j,'anadhar',('hi,6.4')}
>>> type(st)
<class 'set'>
>>> 