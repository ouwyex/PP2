#PYTHON home

print("Hello, World!")

#PYTHON intro

print("Hello, World!")

#PYTHON Get started

import sys

print(sys.version)

#PYTHON syntax

if 5 > 2:
 print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")


#PYTHON Comments

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

#PYTHON variables

a = 4
A = "Sally"
#A will not overwrite a

#variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#assign multiple variablles
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#output multiple variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#global variables
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


#PYTHON Data types

x = 5
print(type(x))

#PYTHON Numbers

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#PYTHON Casting

x = int(1)   # x will be 1
y = float("3")   # z will be 3.0
z = str(3.0)  # z will be '3.0'

#PYTHON strings

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#slicing
b = "Hello, World!"
print(b[-5:-2])

#modifying
a = "Hello, World!"
print(a.upper())
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#concatenating
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#formating
txt = f"The price is {20 * 59} dollars"
print(txt)

#escaping
txt = "We are the so-called \"Vikings\" from the north."
