# list=[1,2,3,"Hari", "prakash", "akash"]
# print(list)


# list=[1,2,3,"Hari", "prakash", "akash"]
# print(list[3])

# list=[1,2,3,"Hari", "prakash", "akash"]
# list.append("apple")
# print(list)

# list1=[1,2,3]
# list2=["apple","Ball","Cat"]
# list1.append(list2)
# print(list1)

# list=[2,3,[5,7,8]]
# print(list[0:2])
# print(list[2][1:3])



# list=[2,3,4,5,"apple"]
# remove=list.pop(4)
# list.append("Ball")
# print(list)


# list=[1,2,3,4,"Apple"]
# list[2]="ball"
# print(list)


# list=[7,8,9,1,2,"H","B","C"]
# print(list[2:6:3])


# list=["Ram","Shyam","hari"]
# if "Shyam"in list:
#     print(f"Shyam present")
# else:
#     print(f"Shyam is not present")

    
# list=[1,2,3,4,5,6,7,8,9,10]
# print(f"list in odd number{list[0:10:2]}",f"and list in even number{list[1:10:2]}")


# list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# for n in list:
#     if(n%2)==0:
#         print(f"even {n}",end=" ")
#     elif (n%2)==1:
#         print(f"\nodd {n}",end=" ")

# lst=[5,4,3,1,6,7,9,8,2]
# def even_odd(lst):
#     even=[]
#     odd=[]
#     for i in lst:
#         if i%2==0:
#             even.append(i)
#         else:
#             odd.append(i)
#     output=[even,odd]
#     return output
# print(even_odd(lst))


# list1=[11,2,3,4,5,6,7,8,9,10]
# print(min(list1))
# print(max(list1))
# 

# list2=[3,5,7,9,3,2]
# list2.sort()
# print(list2)

# list3=[1,2,3,4,5,6,7,8,9,10]
# list3.pop(5)
# print(list3)

# list4=[1,2,3,4,5,6,7,8,9,10]
# list4.reverse()
# print(list4)


# list5=[1,2,3,4,5,6,8,9]
# max=list5[1]
# for i in (list5):
#     if i>max:
#         max=i
# print(f"Max number is: {max}")

# list6=[1,2,3,4,5,6,7,8,9]
# max=list6[0]
# for i in range(len(list6)):
#     if list6[i]>max:
#         max=list6[i]
# print(f"Max number is: {max}")



# lst1=[1,2,3,4,5,6,7,8,9,10]
# def lstrev(list1):
#     list=[]
#     for i in range(len(lst1)):
#         val=lst1.pop()
#         list.append(val)
#     return(list)
# print(lstrev(lst1))


# lst2=['abc','def','ghi']
# def lstrev(lst2):
#     lst3=[]
#     for i in range(len(lst2)):
#         val=lst2.pop()
#         lst3.append(val[::-1])
#     return(lst3)
# print(lstrev(lst2))

# list3=['abc','def','ghi']
# def lstrev(list3):
#     list4=[]
#     for i in range(len(list3)):
#         ver=list3[i]
#         list4.append(ver[::-1])
#     return(list4)
# print(lstrev(list3))

# list12=[1,2,3,[4,5,6],7,8,[9,10,11],12,13,[14,15]]
# def fun(list12):
#     count=0
#     for i in range(len(list12)):
#         if type(list12[i]) is type(list12):
#             count=count+1
#     return(count)
# print(fun(list12))
