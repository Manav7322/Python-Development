# higher order function 
# def greet(func):
#     func()

# def greet2():
#     def func():
#         return 5
#     return func()

def my_decorator(func):
    def wrap(*args,**kwargs):
        func(*args,**kwargs)
    return wrap
@my_decorator
def hello(greeting,emoji=':('):
    print(greeting,emoji)

hello("namaste",':)')


