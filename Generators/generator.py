# def generator_function(num):
#     for i in range(num):
#         yield i*3
# # for item in generator_function(1000):
# #     print(item)
# g=generator_function(100)
# print(g)

# def special_for(iterable):
#     iterator=iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             next(iterator)
#         except StopIteration:
#             break

# special_for([1,2,3])

class MyGen():
    current=0
    def __init__(self,first,last):
        self.first=first
        self.last=last

    def __iter__(self):
        return self
    def __next__(self):
        if MyGen.current< self.last:
            num=MyGen.current
            MyGen.current+=1
            return num
        raise StopIteration



gen=MyGen(1,4)
for i in gen:
    print(i)