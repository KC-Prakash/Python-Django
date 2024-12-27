while 1:
    print("what would you like to do:-")
    print("1. Adition")
    print("2. Sub")
    print("3. Multipliction")
    print("4. Division")
    print("5. exit")
    choice=int(input("Enter a title1: "))
    if choice ==1:
        a=int(input("Enter a number : "))
        b=int(input("Enter a number : "))
        sum=a+b
        print(f'Addition a,b is {sum}')
    elif choice ==2:
        a=int(input("Enter a number : "))
        b=int(input("Enter a number : "))
        sub=a-b
        print(f'Subtraction a,b is {sub}')
    elif choice ==3:
        a=int(input("Enter a number : "))
        b=int(input("Enter a number : "))
        mul=a*b
        print(f'Multipliction a,b is {mul}')
    elif choice ==4:
        a=int(input("Enter a number : "))
        b=int(input("Enter a number : "))
        div=a/b
        print(f'Division a,bis {div}')
    elif choice>=5:
        print("Exit")
        break



# while 1:
#     print("What would you like to do:-")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Exit")
#     choice = int(input("Enter a number: "))
    
#     if choice == 1:
#         a = int(input("Enter a number: "))
#         b = int(input("Enter a number: "))
#         sum_result = a + b
#         print(f'Addition of a and b is {sum_result}')
        
#     elif choice == 2:
#         a = int(input("Enter a number: "))
#         b = int(input("Enter a number: "))
#         sub_result = a - b
#         print(f'Subtraction of a and b is {sub_result}')
        
#     elif choice == 3:
#         a = int(input("Enter a number: "))
#         b = int(input("Enter a number: "))
#         mul_result = a * b
#         print(f'Multiplication of a and b is {mul_result}')
        
#     elif choice == 4:
#         a = int(input("Enter a number: "))
#         b = int(input("Enter a number: "))
#         if b == 0:
#             print("Error! Division by zero.")
#         else:
#             div_result = a / b
#             print(f'Division of a and b is {div_result}')
    
#     elif choice == 5:
#         print("Exiting...")
#         break
        
#     else:
#         print("Invalid choice! Please enter a valid number between 1 and 5.")
