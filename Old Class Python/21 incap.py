


# Access Modifier
# Publish
# private
# protrcted


# class Employe:
#     def __init__(self,name,salary,project):
#         self.name=name #(public member(accessible within or outside class))
#         self._salary=salary #protected member(accessible within the class and its sub class)
#         self.__project=project #private(accessible only within a class)
# emp=Employe("Prakash",10000,"Projectabc")
# print(emp._Employe__project)
# print(emp._salary)





# class Employe:
#     def __init__(self,name,salary,project):
#         self.name=name
#         self._salary=salary
#         self._project=project
# class office(Employe):
#     def __init__(self,name,_salary,_project,address,noemp):
#         Employe.__init__(self,name,_salary,_project)
#         self.address=address
#         self._noemp=noemp

#     def full_detail(self):
#         print(f"{self.name} {self._salary} {self._project} {self.address} {self._noemp}")
# emp=office("Prakash", 10000, "Python", "Butwal", 100)
# emp.full_detail()



# class student:
#     def __init__(self,name,age):
#         self.name=name
#         self.__age=age
#     def get_age(self):
#         return self.__age

#     def set_age(self,age):
#         self.__age=age

# std=student("Prakash",32)
# print("name", std.name,std.get_age())
# std.set_age(55)
# print("name",std.name, std.get_age())



# class staff:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary

#     def show_detail(self):
#         print("name",self.name)
#         print("age",self.age)
#         print("roal",self.roal)
#         print("dept",self.dept)
# class teachers(staff):
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        
#         super().__init__("teacher","Scince",25000)
# teacher=teachers("Raj",25)
# print(teacher.__dict__)



class rectangle:
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    
    def parameter(self):
       return 2*(self.length+self.breath)
    
    def area(self):
        return self.length*self.breath
    
    def full_detail(self):
        print("the lenth is", self.length)
        print("breath is",self.breath)
        print("area is",self.area())
        print("parameter is",self.parameter())
class volume(rectangle):
    def __init__(self,length,breath,height):
        rectangle.__init__(self,length,breath)
        self.height=height
    def vols(self):
        return (f"volums is {self.length*self.breath*self.height}")

obj=rectangle(2,5)
obj.full_detail()
vol=volume(10,10,5)
print(vol.vols())

