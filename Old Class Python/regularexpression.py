# import re
# str="there is sunny outside butwal. The temperatur have reached to 40"
# res=re.findall(r"\d",str)
# print(res)
                    #re.I
                    # re.IGNORECASE
# import re
# target_string="Prakash is a python developer at butwal companey. PRAKASH lover meaching learing and artifical intelanges"
# # wirhout case insensetive
# result=re.findall(r"Prakash",target_string)
# print(result)
# #with re.I
# result=re.findall(r"Prakash",target_string,re.I)
# print(result)
# #wirh re.ignorecase
# result=re.findall(r"Prakash abc",target_string,re.IGNORECASE)
# print(result)

# result=re.findall(r"\bPrakash\b|\bdeveloper\b|\bbutwal\b",target_string,re.IGNORECASE)
# print(result)



# import re
# target_string="Prakash is a python developer at butwal companey. PRAKASH lover meaching learing and artifical intelanges"
# result=re.search(r"\w{9}",target_string)
# result=re.search(r"PRAKASH",target_string)
# print(result)


# import re
# target_string="Prakash is a python developer at butwal companey. PRAKASH lover meaching learing and artifical intelanges"
# result=re.match(r"\b\w{7}\b",target_string)
# print(result)


# for i in range(5):
#     print("*")

# for i in range(5):
#     print("*",end=" ")
# print()
# for i in range(5):
#     print("*",end=" ")
# print()

# for i in range(5):
#     print("*",end=" ")
# print()

# for i in range(5):
#     print("*",end=" ")
# print()

# for i in range(5):
#     print("*",end=" ")
# print()
# n=5
# for i in range(5):
#     for j in range(5):
#         print("*",end=" ")
#     print()
# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")


#     print()


# n=5
# for i in range(5):
#     for j in range(i,n):
#         print("*",end=" ")


#     print()

# n=5
# for i in range(5):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(n-i):
#         print("*",end=" ")


#     print()

# n=5
# for i in range(n):

#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()


n=6
for i in range(n):

    for j in range(n-i):
        print(" ",end=" ")
    for j in range(i*2):
        print("*",end=" ")
    print()
