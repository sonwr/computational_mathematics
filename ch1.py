# ------------------------------------------
# 1.1 Basic Python
# ------------------------------------------
# 1.1.1 Python, numbers and variables
# ------------------------------------------
print('Hello world!')

x = 1.9
print (type(x))


# ------------------------------------------
# 1.1.2 Basic mathematical operations
# ------------------------------------------

# Examples of Arithmetic Operators 
x = 11
y = 2

# Addition of numbers 
add = x + y 
# Subtraction of numbers  
sub = x - y
# Multiplication of numbers  
mul = x * y 
# Division (float) of numbers  
div1 = x / y
# Division (floor) of numbers
div2 = x // y
# Modulo of both numbers 
mod = x % y 
# Raise to power
pow = x ** y

# print results 
print( 'add = ', add ) 
print( 'sub = ', sub ) 
print( 'mul = ', mul ) 
print( 'div1 = ', div1 ) 
print( 'div2 = ', div2 ) 
print( 'mod = ', mod ) 
print( 'pow = ', pow ) 


# ------------------------------------------
# 1.1.3 Mathematical functions and constants
# ------------------------------------------
import math
print(math.sin(math.pi/5))

from math import *
print(sin(pi/5))

import math as mt
print( mt.sin(mt.pi/5))

import math as mt
print(4.0*mt.atan(1.0))

from math import atan
print(4.0*atan(1.0))


# ------------------------------------------
# 1.1.4 Powers of 10 and scientific notation
# ------------------------------------------
print (1.0+1.e-16)
print (1.0+1.e-5)



# ------------------------------------------
# 1.3 Strings, Tuples, Dictionaries and Lists
# ------------------------------------------
# 1.3.1 Strings
# ------------------------------------------
my_name = 'James'
print( my_name[:] )
print( my_name[0:5] )
print( my_name[:5] )
print( my_name[3:] )

# ------------------------------------------
# 1.3.2 Tuples
# ------------------------------------------
x = ( 2, 'Hi' )
print( x[0] )
print( x[1] )


# ------------------------------------------
# 1.3.3 Dictionaries
# ------------------------------------------
variables = { \
"x": 0, \
"y": 1, \
"z": 2 \
}

print( variables["x"] )

variables["y"] = 10
print( variables["y"] )


# ------------------------------------------
# 1.3.4 Lists
# ------------------------------------------
list = [5, 3, 7]
print(list[0])
print(list[1])
print(list[2])
print(list[-1])

list[1] = 9
print(list)

list.append(10)
print(list)

list2 = [9, 6, 8, 7, 9, 7]
list1 = list2
list2[1] = 10
print(list1)
print(list2)

list2 = [9, 6, 8, 7, 9, 7]
list1 = list2[:]
list2[1] = 10
print(list1)
print(list2)


# ------------------------------------------
# 1.4 Flow Control
# ------------------------------------------

for i in [0, 1, 2]:
    print('Hello world!')

for i in [0, 1, 2]:
    print(i)

for i in range(3):
    print(i)


# ------------------------------------------
# 1.7 Accessing Data Files
# ------------------------------------------

f = open("test.txt", "w")
for i in range(5):
    f.write(str(i)+'\n')
f.close()

