import datetime

# none
haveCar = None

# int, float, complex
age = 32
height = 3.7
cmp = 1+2j

# string
name = "Ali"

# bool
married = False

# datetime
# x = datetime.datetime.now()
dt = datetime.datetime(2020, 5, 17)
print(dt)
print(dt.year)
print(dt.strftime("%A"))

# list, set, tuple, dict
l = ["apple", "banana", "cherry"]
s = {"apple", "banana", "cherry"}
t = ("apple", "banana", "cherry")
d = {"name": "John", "age": 36}

# range()
range(0, 10, 2)

# find the type of a variable
print(type(1))
