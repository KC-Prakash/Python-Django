# def sum(x,y):
#     return(x+y)
# print(sum(10,10))
# print(sum(15,15))

# num=15
# def even_odd(num):
#     if num%2==0:
#         return("even")
#     else:
#         return("odd")
# print(even_odd(num))


# num=int(input("Enter a number"))
# def even_odd(num):
#     if num%2==0:
#         return("Even")
#     else:
#             return("odd")
# print(even_odd(num))


# a=input("Enter a name:")
# def name_print(a):
#     return a[-0]
# print(name_print(a))


# a=20
# def sub (a,):
#     # a=10
#     b=5
#     return(a-b)
# print(sub(a))


# name=input("Enter a name: ")
# def print_name(name):
#     return name[::-1]
# print(print_name(name))


# a=int(input("Enter first Number: "))
# b=int(input("Enter a second number: "))
# def grater(a,b):
#     if a>b and a!=b:
#         return (f"a is gerater b:")
#     elif a<b and a!=b:
#         return (f"b is grater a:")
#     elif a==b:
#         return (f"a and b are equal")
# print (grater(a,b))




# a=int(input("Enter first number: "))
# b=int(input("Enter second number: "))
# c=int(input("Enter a third number: "))
# def grater_or_Equal(a,b,c):
#     if a>b and a>c:
#         return(f"Firest number is gratest second and third: ")
#     elif b>a and b>c:
#         return(f"Second number is gratest first and third: ")
#     elif c>a and c>b:
#         return(f"Third number is gratest first and second: ")
#     elif a==b==c:
#         return(f"three number is equal: ")
#     elif (a==b) and ((a==b)!=c):
#         return(f"first and second are equal: ")
#     elif (b==c) and ((b==c)!=a):
#         return(f"first and third are equal: ")
#     elif (c==a) and ((c==a)!=b):
#         return(f"first and third are equal: ")
# print (grater_or_Equal(a,b,c))




# num=int(input("Enta a number"))
# def multiply(num):
#     for i in range(1, 11):
#         print(num, 'x',i, '=', num*i)
# multiply(num)


# num=input("Enter a number")
# def sum(num):
#     total=0
#     for i in range(len(num)-1):
#         total=total+int(num[i])
#     print(total)
# sum(num)


# a=input("Enter a name and number")
# def find_palindrome(a):
#     revname=a[::-1]
#     print(type(revname))
#     if a==revname:
#         print(f"this is palindrom {a}")
#     else:
#         print(f"this is not palindron {a}")
# find_palindrome(a)


n=int(input("Enter a number:"))
def find_palindrome(num):
    temp=num
    rev=0
    while(num>0):
        rem=num%10
        rev=rev*10+rem
        num=num//10
    if temp==rev:
        print(f"this is palindrom")
    else:
        print(f"this is not palindrom")
find_palindrome(n)

