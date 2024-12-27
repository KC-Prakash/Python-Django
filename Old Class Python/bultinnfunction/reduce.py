from functools import reduce
str=[65,75,85,95,100]
var=reduce(lambda a,b: a+b, str)
print(var)




