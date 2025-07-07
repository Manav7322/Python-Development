#Fundamental Data types
#int #represent all integers
print(type(2+4)) #it tells us what datatype is the result.
print(type(2-4))
print(type(2*4))
print(type(2/4)) #this will result in float as 2/4 is 0.5
# float # represent all floating numbers

# we usually use int because it takes less memory as compared to the float
# https://docs.python.org/3/tutorial/floatingpoint.html here is the link for floating ppint number limitatiomns in python. 
print(2**2) #2 to the power 2
print(2//4) #its the same as 2/4 but it return integer number only
print(6%4) #returns remainder.
# bool # return true or false

# str #represents all the strings
# list #represents a list of data for eg. a list of numbers and all.
# tuple A tuple in Python is an ordered and immutable collection of elements. 
# It is one of Python's built-in data types for storing collections of data, 
# alongside lists, sets, and dictionaries
# set stores data like a list the main key differece between the list 
# and set is set doesn't store the duplicate value in it
# dict stores data in the form of key and value key should be unique
#  but value may repeats 

#classes->custom types

#specialized datatypes
#Modules or we can say extensions

#None its simply nothing

# Math Functions
print(round(3.9))
print(abs(-20))
#  https://docs.python.org/3/library/math.html
# above is the wiki where you can find different types of math functions python 3 has 

#operator precedence
print(20-3*4)
#order
#()
#**
#*
#/
#+ -

# complex datatype - its the type which we learn in maths consists of 
# real and imaginery number.
bin(4)
print(int('0b100',2)) #converts binary to integer number.
# it converts number into binary 

#Variables
# variables are the ways to store data or i can say information
# for example
a = 10
print(a)
# these are the syntax or i can say the ways to declare a variable
# 1.snake_case
# 2.Start with lowercase or underscore
# 3.Letters, numbers, underscores
# 4.Case sensitive
# 5.Don't overwrite Keywords

#augmented assignment operator
b = 4
b = b + 3
# or i can also write this 
b += 3
print(b)

# strings data type 
username = 'supercoder'
print(type(username)) #returns the type which is string.

# Multiline string 
long_string='''
WOW
0 0
---
'''