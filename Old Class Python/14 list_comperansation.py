# list=[1,2,3,4,5,6,7,8,9,10]
# list=[i**2 for i in list]
# print(list)

# list=[1,2,3,4,5,6]
# list2=[]
# rev=[list2.insert(0,i) for i in list]
# print(list2)


# list=[1,2,3,4,5,6,7,8,9]
# list2=[]
# rev=[list2.append(i) for i in list[::-1]]
# print(list2)


# list=['abc','def','ijk']
# list2=[]
# rev=[list2.append(i) for i in list[::-1]]
# rev=[i[::-1]  for i in list]
# print(rev)


# list=[i for i in range(1,21) if i%2==0]
# print(list)

# list=[i for i in range(1,21) if i%2==1]
# print(list)




# ver=[7.5, 6.8, -4.6, 9, -2.3]
# list=[i if i>0 else 0 for i in ver]
# print(list)

# new_list=['huit','prakash',6,7,8.2,5,6.9,6.6]
# def typ(new_list):
#     lst=[i for i in new_list if type(i)==int or type(i)==float]
#     return(lst)
# print(typ(new_list))

# new_list=['huit','prakash',6,7,8.2,5,6.9,6.6]
# def typ(new_list):
#     lst=[i for i in new_list if type(i)==str]
#     return(lst)
# print(typ(new_list))

# odd=[]
# even=[]
# ver=[even.append(i) if i%2==0 else odd.append(i) for i in range(1,10) ]
# print(odd, even)


# st1="America"
# st2="Japan"
# def concat(st1,st2):
#     first_char=st1[0]+st2[0]
#     mid_char=st1[int(len(st1)/2):int(len(st1)/2+1)]+st2[int(len(st2)/2):int(len(st2)/2+1)]
#     last_ch=st1[int(len(st1)-1)]+st2[int(len(st2)-1)]
#     final_char=first_char+mid_char+last_ch
#     return(final_char)
# print(concat(st1,st2))

# st1="America"
# st2="Japan"
# first_char=st1[0]+st2[0]
# mid_char=st1[int(len(st1)/2):int(len(st1)/2+1)]+st2[int(len(st2)/2):int(len(st2)/2+1)]
# last_ch=st1[int(len(st1)-1)]+st2[int(len(st2)-1)]
# final_char=first_char+mid_char+last_ch
# print(final_char)


# str="Amirica"
# char=str[0]+str[int(len(str)/2):int(len(str)/2+1)]+str[int(len(str)-1)]
# char=str[0]+str[len(str)//2]+str[len(str)-1]
# print(char)


# ver={i:i**3 for i in range(1,5)}
# print(ver)



# set1={1,2,3,4,5,6,7}
# set2={10,5,15,11,13}
# print(set1|set2) 
# print(set1&set2)


# tup1=(1,2,3,4)
# tup2=(5,6,7,8)
# tup1,tup2=tup2,tup1
# print(f'tup1 is {tup1}')
# print(f'tup2 is {tup2}')


# dict={"a":100,"b":200,"c":300}
# val=200
# if val in dict.values():
#     print("200 present")
# else:
#     print("200 doesnet present")









