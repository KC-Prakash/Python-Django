# lst=[1,2,3,4,5,6,7,8,9,10]
# odd=filter((lambda n:n%2==1),lst)
# for i in odd:
#     print(i)

# lst=[1,2,3,4,5,6,7,8,9,10]
# odd=list(filter((lambda n:n%2==1),lst))
# print(odd)


# lst=[1,2,3,4,5,6,7,8,9,10]
# odd=list(map((lambda n:n%2==1),lst))
# print(odd)

lst=[1,2,3,4,5,6,7,8,9,10]
odd=list(map((lambda n:n*2),lst))
print(odd)