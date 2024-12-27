# def sum(a,b):
#     sum=a+b
#     return sum
# print(sum(10,20,10))


# def sum (a,b,*args):
#     print(a)
#     print(b)
#     print(args)
#     print(type(a))
#     print(type(args))
# sum(10,20,30,40,50)



# def sum(*args):
#     total=0
#     for i in args:
#         total=total+i
#     print(total)
# sum(10,20,30,40,50,60,70,80,90,100)
# sum(1,2,3,4,5)



# def num(*args):
#     mult=1
#     for i in args:
#         mult=mult*i
#     print(mult)
# num(1,2,3,4,5,6)


#(normal paramater,*args,defult paremater,**kwargs)



# def sqr1(n1,*args):
#     if args:

#         sqr=[i**n1 for i in args]
#         print(sqr)
#     else:
#         print("you didn't pass the argument")

# sqr1(2,10,20,30,40,50,60,70,80,90,100)
# # sqr1(2)


# **kwargs

# def fun(**kwargs):
#     for i,j in kwargs.items():
#         print(f"{i}:{j}")
# fun(Name="Sagar",Age=25,Address="Butwal")


# def fun(n,*args,b=5,c=10,**kwargs):
#     sum=n+b+c
#     print(sum)
#     total=0
#     for i in args:
#         total+=i
#     print(total)
#     for i,j in kwargs.items():
#         print(f'{i}:{j}')
# fun(5,5,10,9,name="Ram",Address="butwal",Age=25)

