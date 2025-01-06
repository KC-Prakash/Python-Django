# File Handling:
"""
# File modes during file handling
1. Read -> means viewing existing data from a file -> 'r'
2. Write -> means adding new data to a file -> 'w'
3. Append -> means adding new data to an existing file -> 'a'
 """


# Reading a text file
# 1-step -> Opening a file
# student_file = open("students.txt", "r")

# 2-step -> read file contents
# print(student_file.read())
# print(student_file.readlines())

# 3-step -> close file
# student_file.close()


# def clean_line(line):
#     return line.strip()



# def show_students_names(file_name):
#     student_file = open("students.txt", "r")
#     students = student_file.readlines()

#     for student in students:
#         student = clean_line(student)
#         print(student)

# def show_students_names(file_name):
#     with open(file_name, "r") as student_file:
#         students = student_file.readlines()

#         for sn, student in enumerate(students, start=1):
#             student = clean_line(student)
#             print(f'{sn}. {student}') 



# def get_all_students(file_name):
#     with open(file_name, "r") as student_file:
#         students = student_file.readlines()
#         # clean each line using map
#         students = list(map(clean_line, students))
#         return students



# with open("students.txt", "w") as student_file:
    # student_file.write("New student\n")    
    # student_file.write("New studentasd\n")    
    # student_file.write("New student\n")    
    # student_file.write("New student\n") 

    #simply use writelines() function to insert multiple lines at a time
    # new_students_list = ['ram\n', 'shyam\n', 'hari\n']
    # student_file.writelines(new_students_list) 
    # 

# def add_single_student(file_name):
#     student_name = input("Enter name of student: ")
#     with open(file_name, "a") as student_file:
#         student_file.write(f"{student_name}\n")    


# def add_multiple_students(file_name):
#     student_list = []

#     while True:
#         print("1. Add New Student")
#         print("2. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             student_name = input("Enter name of student: ")
#             student_list.append(f"{student_name}\n")
#         else:
#             break

#     with open(file_name, "a") as student_file:
#         student_file.writelines(student_list)   


# def delete_student(file_name):
#     student_name = input("Enter name of student: ")
#     with open(file_name, "r") as student_file:
#         students = student_file.readlines()
    
#     with open(file_name, "w") as student_file:
#         for student in students:
#             if student_name not in student: #"ram" == "ram kumar"
#                 student_file.write(f"{student}")



# add_multiple_students("students.txt")

# delete_student("students.txt")
# show_students_names("students.txt")
# print(get_all_students("students.txt"))


# Read and Write operations with csv files
# import csv

# with open("prices.csv", "r") as price_file:
#     price_reader = csv.reader(price_file)
#     for product, price in price_reader:
#         print(product, price)

# def give_seperated_data(lines):
#     return [clean_line(line).split("|") for line in lines]

# with open("students.txt", 'r') as student_file:
#     lines = student_file.readlines()
#     seperated_data = give_seperated_data(lines)

#     # print(seperated_data)
#     for student, number in seperated_data:
#         print(f"{student} - {number}")

# def copy_text_file(file_name):
#     with open(file_name, "r") as source_file:
#         lines = source_file.readlines()

#     with open(f"{file_name.replace('.txt', '')}_copy.txt", "w") as copy_file:
#         copy_file.writelines(lines)


# copy_text_file("students.txt")







# Error Handling or Exception Handling
# print(9/0)
# print("lskdfjlksdf")
'''
1. try-block -> write code that might cause an error
2. except-block -> write code that will handle the error
3. else-block -> write code that will execute if there is no error
4. finally-block -> write code that will execute regardless of whether there is an error or not
'''


# try:
#     print(9/"0")
# except ZeroDivisionError:
#     print("Sorry, you cannot divide by zero")
# # except TypeError:
# #     print("Both numerator and denominator should be integers/floats")
# except Exception:
#     print("Something went wrong, please try again later")

# print("lskdfjlksdf")

# try:
#     file = open("studen.txt", "r")
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print("Something went wrong, please try again later")
# else:
#     print(file.read())
# finally:
#     file.close()




# import os
# import time
# while True:
#     number1 = int(input("Enter num1: "))
#     number2 = int(input("Enter num2: "))

#     try:
#         result = number1 / number2
#     except ZeroDivisionError:
#         os.system("cls")
#         print("Sorry, you cannot divide by zero")
#         time.sleep(2)
#         os.system("cls")
#     else:
#         print(result)
#         break
    

