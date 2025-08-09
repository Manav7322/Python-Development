# # nums=[2,5,7,1,9]
# # print(nums)
# # print(*nums) #unpacking

# def order_pizza(size, *toppings, **details):
#     print(f"ordered a {size} pizza with a following toppings")
#     for topping in toppings:
#         print(f"-{topping}")
#     print("\nDetails of the order are:")
#     for key,value in details.items():
#         print(f"-{key}: {value}")

# order_pizza("large", "tomato", "onion", "cheese", delivery=True, tip=5)

def log_args(func):
    def wrapper(*args, **kwargs):
        print(f"Function '{func.__name__}' was called with:")
        print(" Positional args:", args)
        print(" Keyword args:", kwargs)
        return func(*args, **kwargs)
    return wrapper

@log_args
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Manav", greeting="Hi")
