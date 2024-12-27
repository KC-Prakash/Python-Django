import random
def get_rendom_number():
    random_number=random.randint(0,9)
    return random_number
print("++==++  Welcome to Number Guessing Game  ++==++")
chance=0
while 1:
    choice=input("Do you want play(Y/N):- ")
    if'y' in choice.lower():
        print("Generating random number")
        random_number=get_rendom_number()
        while 1:
            user_number=int(input("Enter the number ypu think:- "))
            chance+=1
            if user_number>9 or user_number<0:
                print("Invalid input")
            else:
                if user_number==random_number:
                    print("Congratulation you win the game in {0} \n".format(chance))
                    chance=0
                    break
                elif user_number>random_number:
                    if abs(user_number-random_number)<=4:
                        print("closer but not cigar, try a lower number")
                    else:
                        print("not even close try a lower")
                elif user_number<random_number:
                    if abs(user_number-random_number)>=4:
                        print("closer but not cigar, try a higher number")
                    else:
                        print("not even close try a higher")
    elif 'n' in choice.lower():
        print("exiting")
        break
    else:
        print("invalid input")