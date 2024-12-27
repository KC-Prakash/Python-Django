# 1)Print these following lines using escape character:
# This is \\ double backslash
# print(f'this is \\\\ double backslash')     #Ans This is \\ double backslash
# This is /\/\/\/\/\ mountain
# print(f'this is///\///\///\///\ mountain')   #Ans /\/\/\/\/\
# \’ \\’
# print('/\'//\'')          #Ans \’ \\’


# 2)Ask User to input 3 number and print the average of three number using string formatting. (use split function) 
# a,b,c=(input("Enter a number a,b,c: ")).split(",")
# average=(int(a)+int(b)+int(c))/3
# print(average)                      #2,5,9=5.333


# 3)Ask user to input name and print back username in reverse order.
# name=input("Enter a name: ")
# print(name[::-1])           #Ans Prakash = hsakarP


# 4)Ask two input from user:
# Sequence of character
# Single character  
# And count character that user inputed from sequence of character.


# 5)Ask a user to input username and print username in given manner (*****Username*****)
# user=input("Enter a name: ")
# print(user.center(len(user)+10,"*"))            #Ans Prakash = *****Prakash*****

# 6)Take a name and age as input and  print you are eligible for vote if age greater or equal to 18 and name starts with “A” ( A is case insensitive)
# age=int(input("Enter a age: "))
# if(age>=18):
#     print("you are eligible for vote")
# else:
#     print("you are not eligible for vote")


# 7)Write program to print sum of first 10 natural number using while loop.
# a=1
# total=0
# while(a<=10):
#     total=total+a
#     a=a+1
# print(total)            #ans 55


# 8)Ask user to input a number and find sum of give input number using while loop
# num=int(input("Enter a number: "))
# a=1
# total=0
# while(a<=num):
#     total=total+a
#     a=a+1
# print(total)          #Ans 10 =55


# 9)Ask user to input username and print count of each word using for loop.  (a:1 b:3 c:2 d:1)
# checkname=" "
# c=0
# name=input("Enter a name: ")
# for i in range(len(name)):
#     if name[c] not in checkname:
#         checkname+=name[c]
#         print(f'{name[i]}: {name.count(name[i])}',end=" ")
#     c=c+1


# 10)Ask a user to input number print the number is even or odd using function
# num=int(input("Enter a natural Number: "))
# if(num%2==0):
#     print('Number is even')
# else:
#     print("Number is odd")


# 11)Ask user to input string check whether given string is palindrome or not using function.
# pal=input("Enter the word and see if it is palindrome: ")
# if pal==pal[::-1]:
#     print("This word is Palindrome")  #ansmalayalam=This word is Palindrome
# else:
#     print("This word is not palidrome")


# 12)Given list=[‘abc’,’def’,’ghi’] print out in following ways [‘ cba’,’fed’,’ihg’ ]
# list=['abc','def','ghi']
# def listrev(list):
#     list0=[]
#     for i in range(len(list)):
#         val=list[i]
#         list0.append(val[::-1])
#     return(list0)
# print(listrev(list))


# 13)Given list=[1,2,3,4,5,6,7,8,9,10] print output in following ways [[2,4,6,8] [1,3,5,7,9]]
# list=[1,2,3,4,5,6,7,8,9,10]
# print(f"{list[0:10:2]}",f"{list[1:10:2]}")



# 14) Given list =[1,2,3,[2,1],[4,5],4,5,[4,7,8,9],4,1] count total number nested list.
# list=[1,2,3,[2,1],[4,5],4,5,[4,7,8,9],4,1]
# def fun(list):
#     count=0
#     for i in range(len(list)):
#         if type(list[i]) is type(list):
#             count=count+1
#     return(count)
# print(fun(list))                #Ans 3



# 15)Ask user to input name and print in following ways {N:1,A:1,M:1,:E:1}
# strings=input("Enter a Name")
# dict={}
# def s_count(strings):
#    for i in strings:
#       dict[i]=strings.count(i)
#    return(dict)
# print(s_count(strings))



# 16)Print dictionary on following way {1:1,2:4,:3:9,4:16,5:25}
# sqr={}
# def sqr1():
#    for i in range(1,6):
#       sqr[i]=i**2
#    return sqr
# print(sqr1())



# 17)Reverse a given list [1,2,3,4,5] using list comprehenses.
# list=[1,2,3,4,5]
# list1=[]
# rev=[list1.append(i) for i in list[::-1]]
# print(list1)


# 18)Given list [“hubit” ,[1,2,3,4], 1.4,12,1.68,14,15] print only interger and float number from given list inside list using list comprehenses
# list=['hubit',[1,2,3,4],1.4,12,1.68,14,15]
# def typ(list):
#     lst=[i for i in list if type(i)==int or type(i)==float]
#     return(lst)
# print(typ(list))

 
 
# 19)Print dictionary on following way {1:1,2:4,:3:9,4:16,5:25} using dictionary comprehenses
# square={i:i**2 for i in range (1,6)}
# print(square)


# 20)Print following using dictionary comprehenses {1:”odd”,2:”even,3:”odd”,4:”even”,5:”odd”,6:”even”}
dict={i:"even" if i%2==0 else "odd" for i in range(1,11)}
print(dict)