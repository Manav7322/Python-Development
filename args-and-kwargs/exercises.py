# Sum of Numbers
# Write a function sum_numbers(*args) that accepts any number of integers and returns their sum.
def sum_numbers(*args):
    addition=0
    for num in args:
        addition+=num
    print(addition)
    return addition
sum_numbers(2,3,4,5,6)

# Concatenate Strings
# Create a function concat_strings(*args) that joins multiple strings with spaces in between.
def concat_strings(*args):
    result=" ".join(args)
    print(result)
    return result
concat_strings("manav", "gupta")

# Keyword Introduction
# Write introduce_person(**kwargs) that prints "Name: <name>, Age: <age>".

# If city is provided, also print "City: <city>".

def introduce_person(**kwargs):
    print(f"Name:{kwargs['name']}, Age:{kwargs['age']}")
    if "city" in kwargs:
        print(f"City: {kwargs['city']}")

introduce_person(name="manav",age="22",city="jammu")

# Menu Order
# Create order_food(main, *sides, **extras) that:

# Prints the main dish.

# Lists sides from *sides.

# Prints extras like sauce type or special notes from **extras.

def order_food(main, *sides, **extras):
    print(f"The main dish is {main}")
    print("The sides are")
    for side in sides:
        print(f"-{side}")
    print("for extras")
    for key,value in extras.items():
        print(f"-{key}:{value}")
order_food("Pizza","coke","cake",base="cheeseBurst",toppings="paneer")


# Shopping Cart
# Function: checkout(*items, **details)

# Print all items.

# Print details (like payment method, delivery option).

def checkout(*items, **details):
    print("Items:")
    for item in items:
        print(f"- {item}")
    print("Details:")
    for k, v in details.items():
        print(f"- {k}: {v}")

checkout("pen","paper",payment_method="online",delivery_option="fast")

# Math Operations

def calculate(operation, *numbers, **options):
    total = 0
    product = 1

    for i in numbers:
        if operation == "+":
            total += i
        elif operation == "*":
            product *= i

    if options.get("round", False): 
        if operation == "+":
            return round(total, 2)
        elif operation == "*":
            return round(product, 2)

    return total if operation == "+" else product


result = calculate("+", 2, 3, round=True)
print(result)

# Dynamic Greeting
# Function: greet_people(greeting, *names, **styles)

# If uppercase=True in **styles, print greeting in uppercase.

# Otherwise, print normally.

def greet_people(greeting, *names, **styles):
    if styles.get("uppercase",False):
        greeting=greeting.upper()
    for name in names:
        print(f'{greeting},{name}')
greet_people("Hello", "Manav", "Riya", uppercase=True)