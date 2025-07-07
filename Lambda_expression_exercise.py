<<<<<<< HEAD
#get the square using lambda
my_list=[5,4,3]
print(list(map(lambda item:item**2,my_list)))

#sorting by the 2nd value in the tuple
a=[(0,2),(4,3),(10,-1),(9,9)]
a.sort(key=lambda x:x[1])
=======
my_list=[5,4,3]
print(list(map(lambda item:item**2,my_list)))

a=[(0,2),(4,3),(10,-1),(9,9)]
a.sort(key=lambda x:x[1])
>>>>>>> ce40167 (create repo and upload the basics of python)
print(a)