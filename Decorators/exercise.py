from functools import wraps
# import time
# from random import randint

# def performance(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         t1=time()
#         result=func(*args,**kwargs)
#         t2=time()
#         print(f'took {t2-t1}sec')
#         return result
#     return wrapper
        
# # @performance
# # def long_time():
# #     for i in range(100000000):
# #         i*5

# # long_time()

# # Retry Decorator
# # Write a decorator retry(times) that retries running the function
# #  up to times times if it raises an exception.

# def retry(times):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args,**kwargs):
#             last_exception=None
#             for attempt in range(1,times+1):
#                 try:
#                     return func(*args,**kwargs)
#                 except Exception as e:
#                     last_exception=e
#                     print(f'Attempt {attempt} failed: {e}')
#                     time.sleep(1)
#             raise last_exception
#         return wrapper
#     return decorator
        

# @retry(3)
# def risky_task():
#     num = randint(1, 10)
#     if num < 8:
#         raise ValueError("Random failure!")
#     print("Success!")

# risky_task()

# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
  # code here
  @wraps(fn)
  def wrapper(user, *args, **kwargs):
        if user.get('valid'):
            return fn(user, *args, **kwargs)
  return wrapper
    


@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)