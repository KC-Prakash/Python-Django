# exception Handling
# try:
#     a=10
#     b=0
#     c=a/b
#     print("the answer is:",c)
# except:
#     print("cant division by zro")


# print(2+"2") Type error
# print(float("five")) value error

# try:
#     a=int(input("Enter a first number"))
#     b=int(input("Enter a second number"))
#     c=a/b
#     print("the answer is",c)
# except ValueError:
#     print("Enter value is wrong")
# except ZeroDivisionError:
#     print("Cant divided by zero")


# try:
#     a=int(input("Enter a first number: "))
#     b=int(input("Enter a second number: "))
#     c=a+b
#     print("Sum of a and b",c)
# except TypeError:
#     print("This is type error")
# except NameError:
#     print("This is name erroe")
# except ValueError:
#     print("this is value error")
# else:
#     print("No found error")

# x=int(input("Enter a first number"))
# y=int(input("Enter a second number"))
# def sum (a,b):
#     if type(a) is int and type(b) is int:
#         return a+b
#     raise ValueError("your values cannot be operate")
# # print(sum(5,"5"))
# print(sum(5,10))


# def simple_intrest(amount,rate,time):
#     try:
#         if rate>100:
#             raise ValueError(rate)
#         intrest=(amount*time*rate)/100
#         print("The simple intrest is", intrest)
#         return intrest
#     except ValueError:
#         print("intrest rate is out of range", rate)
# simple_intrest(98000,4,10)



# num1=input("Enter a first number")
# num2=input("Enter a second number")
# try:
#     num3=int(num1)+int(num2)
# except TypeError:
#     print("this is type error")
# except ValueError:
#     print("This is value error")
# except NameError as thisname:
#     print(f"this is name error {thisname}")
# except ZeroDivisionError as obj:
#     print(obj)
# else:
#     print(num3)


