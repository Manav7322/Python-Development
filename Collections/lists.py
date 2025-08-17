li=[1,2,3,4,5] #list example
li2=['a',1,'b',2] #another list problem

# we can perform various things in lists
# List slicing
#Mutable
amazon_cart=[
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
    ]
print(amazon_cart[0:2:1])

# how to copy a list 
new_cart=amazon_cart[:]
# or 
new_cart=amazon_cart.copy()
new_cart[0]='gum'
print(new_cart)
print(amazon_cart)

#list methods
# length()
print(amazon_cart.__len__())
# or 
print(len(amazon_cart))
#adding append only add the new  object at the end of list
#we can also use insert to add whatever index we want
#extend is the method which append the new list in the existing list.
basket=[1,2,3,28,5]
basket.append(6)
print(basket)

# removing methods
#pop method it by default removes the last element 
# but if  we give it index then it removes that exact element 
#remove method takes the value that you want to remove.
# basket.pop(2)
# basket.remove(4)
print(basket)

# clear-clear all the list and convert it into empty list
# basket.clear()
# print(basket)

#sort method helps in sorting the list
# basket.sort()
# print(basket)

# reverse is a method which reverse the list 
basket.reverse()
print(basket)
