# fp=open("file1.txt","w")
# fp.write("This is my first file hendaling file")
# fp.close()

# fp=open("file.txt","x")
# fp.close

# fp=open("file2.txt","w")
# fp.write("This is a file file handeling")
# fp.close


# import os
# print(os.listdir())
# print(os.path.isfile("file2.txt"))


# with open(r"C:\Users\praka\OneDrive\Desktop\Computer Programing\Python\filehandeling\file.txt","w") as fp:
#     fp.write("This is text file")
#     pass

# import os
# file_path=(r"C:\Users\praka\OneDrive\Desktop\Computer Programing\Python\filehandeling\file3.txt")
# if os.path.exists(file_path):
#     print("File is alredy exist")
# else:
#     with open(file_path,"w") as fp:
#         fp.write("THis is file handeling text file 3")
#         pass



# import os
# file_path=(r"C:\Users\praka\OneDrive\Desktop\Computer Programing\Python\filehandeling\file4.txt")
# if os.path.exists(file_path):
#     print("File is alredy exist")
# else:
#     with open(file_path,"w") as fp:
#         fp.write("THis is file handeling text file 3")
#         print("File is save")
#         pass

try:
    file_path=(r"C:\Users\praka\OneDrive\Desktop\Computer Programing\Python\filehandeling\file3.txt")
    with open (file_path,"x") as fp:
        fp.write("This is file handeling")
        pass
except:
        print("This is alrady exist")




