# name="Hari"
# for i in range(len(name)):
#     print(name[i])


# name="prakash"
# for i in name:
#     print(i)


# nmu=10
# for i in range(1,11):
#     print(i)


# for i in range(10,3,-1):
#     print(i)


# for i in range(1,10,2):
#     print(f"odd number:{i}")

# for i in range(0,11,2):
#     print(f"Even numberis: {i}")


# for i in range(1,11):
#     print(i**2)


# total=0
# for i in range(1,6):
#     total=total+i
# print(total)


# total=0
# num=input("Enter a number: ")
# for i in range(len(num)):
#     total=total+int(num[i])
# print(f"sum of number{total}")


checkname=" "
c=0
name=input("Enter a name")
for i in range(len(name)):
    if name[c] not in checkname:
        checkname+=name[c]
        print(f"{name[i]}: {name.count(name[i])}", end=" ")
    c=c+1


# name=input("Enter a name: ")
# for i in range(len(name)-1,-1,-1):
#         print(name[i],end="")

# name=input("Enter a name")
# for i in range(len(name)-1,1,-1):
#     print(name[i],end="")
