p# user_info=dict({'Name':"XYZ","Sex":"Male","Age":20,"Qualification":"Intermediate level"})
# print(user_info)
# print(type(user_info))


# user={'Name':"Pratik","Age":18,"Sex":"Male","Quelifation":"Bachelor","Hobby":"Singing"}
# print(user)
# print(user["Name"])
# print(user["Quelifation"])
# print(user.get("Hobby"))
# user["Age"]=24
# print(user)
# user["Fev Player"]="Sergio"
# print(user)
# print(user.pop("Age"))
# print(user.popitem())
# print(user)



# dict1={"Name":"Prakash","Address":"Butwal","Age":19,"Hobby":"Game Play"}
# dict2={"Name":"Akash","Address":"Pokhara","Age":25}
# print(f'Dict2{dict2}')
# print(f'Dict1{dict1}')
# dict1.update(dict2)
# print(f'update dict2 in dict 1{dict1}')



# dict={"Name":"XYZ","Age":28,"Sex":"Female","Profession":"Docter","Hobby":["SInging", "Dancing", "Travling"],"Fev Film":"abc"}
# for i in dict.items():
#     print(i)




# d_cub={}
# def cube():
#    for i in range(1,6):
#       d_cub[i]=i**3
#    return d_cub
# print(cube())




# strings=input("Enter a Name")
# dict={}
# def s_count(strings):
#    for i in strings:
#       dict[i]=strings.count(i)
#    return(dict)
# print(s_count(strings))

# list1=['A','B','C','D','E']
# list2=[1,2,3,4,5]
# dict={}
# for i in range(len(list1)):
#    dict.update({list1[i]:list2[i]})
# print(dict)



# list=[["a", 1], ["b",2], ["c",3], ["d",4]]
# dict={}
# for i in list:
#     key=i[0]
#     value=i[1]
#     dict[key]=value
# print(dict)


# dic={"a":[5,4,3,1], "b":[7,6,8,4],"c":[4,7,9,2],"d":[1,2,4,3]}

# for i in dic.values():
#    i.sort()
 
# print(dic)


dic={"name":"ABC", "Address":"XYZ","Hobbies":["dansing","Singing"]} #convert list
list=[(k,v)for k,v in dic.items()]
print(list)
