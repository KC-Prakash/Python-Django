
def show_menu():  #function defination
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Exit")


def perform_add():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(num1+num2)


def perform_sub():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(num1+num2)


def perform_mul():
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    print(num1+num2)


PI = 3.1415



# print("module1's name is", __name__)
if __name__ == "__main__":
    #do something
    show_menu()