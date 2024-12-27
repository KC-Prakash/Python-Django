
# """This is decorator function"""
# def fun1():
#     print("This is function 1")


# def fun2():
#     print("This is function 2")
# fun2()

# def decorator_function(any_function):
#     def wrapper_function():
#         print("Thiis is decorator function")
#         any_function()
#     return wrapper_function

# def fun1():
#     print("This is function 1")


# def fun2():
#     print("This is function 2")

# fun1=decorator_function(fun1)
# fun2=decorator_function(fun2)

# fun1()
# fun2()


# def decorator_function(any_function):
#     def wrapper_function():
#         print("Thiis is decorator function")
#         any_function()
#     return wrapper_function

# @decorator_function
# def fun1():
#     print("This is function 1")

# @decorator_function
# def fun2():
#     print("This is function 2")

# fun1()
# fun2()

# def decorator_function(any_function):
#     def wrapper_function(*args, **kwargs):
#         print("Thiis is decorator function")
#         return any_function(*args, **kwargs)
#     return wrapper_function
    
# @decorator_function
# def fun1(a):
#     print(f"This is function one {a}")

# fun1(8)

# @decorator_function
# def fun2(a,b):
#     return a+b
# print(fun2(5,9))


# from functools import wraps

# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args, **kwargs):
#         """This is doctype string"""
#         print("Thiis is decorator function")
#         return any_function(*args, **kwargs)
#     return wrapper_function

# @decorator_function
# def fun1(a):
#     """this is doctype string function 1"""
#     print(f"This is function one {a}")


# print(fun1.__doc__)
# fun1(5)
# print(fun1.__name__)


# from functools import wraps
# def decorator_function(any_function):
#     @wraps(any_function)
#     def wrapper_function(*args, **kwargs):
#         print("your are calling add function")
#         return any_function(*args, **kwargs)
#     return wrapper_function


# @decorator_function
# def sum(a,b):
#     """this function takes two number as arguments & return there sum"""
#     sum = a+b
#     return sum

    
# print(sum.__doc__)
# print(sum(4,5))

# print(sum.__name__)



