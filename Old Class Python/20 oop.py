# class person:
#     def __init__(self,firstname,lastname,age):
#         self.firstname=firstname
#         self.lastname=lastname
#         self.age=age
#         self.fullname=firstname+ " " + lastname
#     def detail(self):
#         return f"{self.firstname} {self.lastname} {self.fullname} {self.age}"

# firstperson=person("Prakash","KC",32)
# print(firstperson.detail())
# secondperson=person("Radha","Basnet", 29)
# print(f"{firstperson.firstname} {firstperson.lastname} {firstperson.age}")
# print(f"{secondperson.firstname}")





# class Employ:
#     def __init__(self,name,address,degni,salary):
#         self.name=name
#         self.address=address
#         self.degni=degni
#         self.salary=salary
# employdetail=Employ("Prakash","Butwal","Manager",25000)
# print(f"{employdetail.name} {employdetail.address} {employdetail.degni} {employdetail.salary}")


# from ctypes import addressof
# from unicodedata import name


# class mobile:
#     dis_percent=10
#     vat_percent=13
#     def __init__(self,mobilename,model,price):
#         self.mobilename=mobilename
#         self.model=model
#         self.price=price
#     def discount(self):
#         global discountprice
#         discountamount=(mobile.dis_percent/100*self.price)
#         discountprice=self.price-discountamount
#         return(discountprice)
#     def vat(self):
#         global vatamount
#         vatamount=(discountprice*mobile.vat_percent/100)
#         return(vatamount)
#     def total(self):
#         totalamount=self.discount()+self.vat()
#         return(totalamount)
    
#     def full_detail(self):
#         return(f"{self.mobilename}, {self.model}, {self.price}")
# mobileobject=mobile("Nokia", 3110, 25000)
# print(mobileobject.full_detail())
# print(f"The price after allowing discount and vat is{mobileobject.total()}")
    

# class circle:
#     py=3.14
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         circlearea=2*circle.py*self.radius**2
#         return(circlearea)
# circleobj=circle(10)
# print(f"circumference of circle {circleobj.area()}")




# class salary:
#     def __init__(self,name,address, Salary):
#         self.name=name
#         self.address=address
#         self.salary=Salary
#     def allownes(self):
#         allownesamount=self.salary*10/100
#         return(allownesamount)
#     def tax(self):
#         taxamount=self.salary*1.5/100
#         return(taxamount)
#     def total(self):
#         totalamount=self.salary+self.allownes()-self.tax()
#         return(totalamount)
#     def full_detail(self):
#         return(f"{self.name}, {self.address}, {self.salary}")
# salaryobject=salary("Prakash", "Butwal", 32000)
# print(salaryobject.full_detail())
# print(f"Total of salary {salaryobject.total()}")

class mobile:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
class samsung(mobile):
    def __init__(self,name,model,price,ram,camera):
        mobile.__init__(self,name,model,price)
        self.ram=ram
        self.camera=camera
class iphone(samsung):
    def __init__(self,name,model,price,ram,camera,rom):
        samsung.__init__(self,name,model,price,camera,rom)
        self.rom=rom

    def full_detail(self):
        print(f"{self.name} {self.model} {self.price} {self.ram} {self.camera} {self.rom}")
obj=iphone("Galaxy","M10",25090,"2gb","12MF","32GB")
obj.full_detail()



class samsunge:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
        super().__init__(name,model,price)
class iphone():
    def __init__(self,camera,processer,ram):
        self.camera=camera
        self.processer=processer
        self.ram=ram
        super().__init__(camera,processer,ram)
class mobile(samsunge,iphone):
    def __init__(self,name,model,price,camera,processer,ram):
        samsunge.__init__(self,name,model,price)
        iphone.__init__(self,camera,processer,ram)

    def full_detail(self):
        print(f"{self.name} {self.model} {self.price} {self.camera} {self.processer} {self.ram}")
obj=mobile("Galaxy","M10",25090,"2gb","12MF","32GB")
obj.full_detail()



# class person:
#     count=0
#     def __init__(self,firstname,lastname,age):
#         person.count+=1
#         self.firstname=firstname
#         self.lastname=lastname
#         self.age=age
#     @classmethod
#     def count_instance(cls):
#         return f"this instance is {cls.count}"
#     def fulldetail(self):
#         return f"{self.firstname} {self.lastname} {self.age}"
#     def old(self):
#         if self.age>=15:
#             return "you are eligible to vot"
# firstperson=person("abc", "bacx", 23)
# secondperson=person("abg", "bdcx", 30)
# thirdperson=person("abe", "bcxh", 22)
# fourthperson=person("abyc", "bcox", 37)
# fiftherson=person("abcq", "bcpx", 93)
# sixthperson=person("abci", "bcbx", 28)
# seventhperson=person("abpc", "bmcx", 26)
# print(firstperson.fulldetail())
# print(person.count_instance())



# class person:
#     def __init__(self,name,idnumber):
#         self.name=name
#         self.idnumber=idnumber
#     def display(self):
#         print(f"{self.name} {self.idnumber}")
# class employe(person):
#     def __init__(self,name,idnumber,salary,post):
#         self.salary=salary
#         self.post=post
#         person.__init__(self,name,idnumber)
#     def fulldetail(self):
#         print(f"{self.name}, {self.idnumber}, {self.salary}, {self.post}")
# employeeobject=employe("Prakash",10,30200,"MIS Operator")
# employeeobject.display()
# employeeobject.fulldetail()



# class calculationadd:
#     def sum(self,a,b):
#         return a+b
# class calculationmultiply:
#     def multiply(self,a,b):
#         return a*b
# class derived(calculationadd,calculationmultiply):
#     def divide(self,a,b):
#         return a/b
# d=derived()
# print(d.divide(15,30))
# print(d.sum(10,25))
# print(d.multiply(25,25))



# class animal:
#     def walking(self):
#         print("Animal can walk")
#     def eating(self):
#         print("Animal can eat")
# class dog(animal):
#     def barking(self):
#         print("The dog can bark")
#     def eating(self):
#         print("Dong can eat")
#     def walking(self):
#         print("Dog can walk")
# class bird(animal):
#     def eating(self):
#         print("Bird can eat")
#     def flying(self):
#             print("Bird can fly")

# obj_animal=animal()
# obj_dog=dog()
# obj_bird=bird()

# obj_animal.walking()
# obj_dog.walking()
# obj_bird.flying()
