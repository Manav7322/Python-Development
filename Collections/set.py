# set 
# unordered collection of unique objects 
myset={1,2,3,4,5,5,4}
# print(myset)
myset.add(100)
print(myset)
mylist=[1,2,3,4,5,5,6,3]
print(set(mylist))
# print(myset[3]) #does not work in set 

# there are many methods that are worked in set 
# copy()
# difference 
# discard
# difference_update()
# intersection
# isdisjoint
# issubset
# issuperset
# union 

your_set={4,5,6,7,8,9,10}
# print(myset.difference(your_set))
# myset.discard(5)
# print(myset)

myset.difference_update(your_set)
print(myset)