<<<<<<< HEAD
#always return the same output for the same input
#doesn't affect the outside world.

def multiply_by2(li):
    new_list=[]
    for item in li:
        new_list.append(2*item)
    return new_list
=======
def multiply_by2(li):
    new_list=[]
    for item in li:
        new_list.append(2*item)
    return new_list
>>>>>>> ce40167 (create repo and upload the basics of python)
print(multiply_by2([1,2,3]))