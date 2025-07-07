#map,filter,zip and reduce
#map
my_list=[1,2,3]
def multiply_by2(item):
    return item*2
print(list(map(multiply_by2,my_list)))
#filter
def only_odd(item):
    return item%2!=0
print(list(filter(only_odd,my_list)))
#zip
your_list=[10,20,30]
print(list(zip(my_list,your_list)))
#reduce
from functools import reduce
def accumulator(acc,item):
    return acc+item
print(reduce(accumulator,my_list,0))

