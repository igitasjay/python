x = 4       # this is of type int
y = "abc"   # this is of type string

# declaring a variable with a type by casting:
# a: int = 2
a = int(12)
b = str("def")

# get type of variable
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'str'>

# Python allows multiple variable assignments in one line:
x, y, z = "hi", "hey", "hello"
print(x)
print(y)
print(z)

# also, one value to multiple variables.
x = y = z = "hello"
print(x, y, z)

# unpacking: you can extract the values of a collection into variables.
my_list = [ "hi", "hey", "hello" ]
x, y, z = my_list

# output variables: you can output multiple variables at once.
print(x, y, z)
print(x + y + z)

# global variables are variables that are defined outside a function, and can be used anywhere, even inside a function.
w = "weird"
def my_function():
    w = "cool"
    print("python is " + w)
my_function() # call the function.

# global variables retain their value. reassigning them another value inside a function changes its value in that function alone.
print("python is " + w)

# use the global keyword if you want to make a local varibale global.
def my_function():
    global w
    w = "crazy"
    print("python is " + w) # prints: python is crazy
my_function()

# now the new value of the w variable is "crazy"
print("python is " + w)