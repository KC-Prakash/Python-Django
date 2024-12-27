# Python Questions.
# 1. Write a Python program that prints the character at index i in the string's. lf the index is out of range, the program should print "i is out
# of range".If the string is empty, the program should print "Empty String"

# char=input("Enter a character: ")
# indx=int(input("Enter character Index: "))
# i=indx
# if len(char)==0:
#     print("Empty String")
# elif i<len(char):
#     print(char[i])
# else:
#     print("i out of rang")


# 2. Write a Python Program that prints the reversed version of a string. The program must preserve uppercase and lowercase letters. If the string
# is empty, print it intact.

# str=input("Enter a Character: ")
# print(str[::-1])


# 3. Write a Python program that prints the first and last three characters ofthe string s as a single string. If the string has less than six 
# characters, printan empty string (blank output).

# str=input("Enter a character: ")
# if len(str)==0:
#     print("Empty character")
# elif len(str)<6:
#     print("less then six character")
# else:
#     print(str[0:3]+str[len(str)-3:])


# 4. Write a Python program that prints the string s without the characters located at even indices. If the string is empty or only has one 
# character, print it intact.(input="coding” =>output="0ig")

# str=input("Enter a character: ")
# if len(str)==0:
#     print("Empty Str ")
# elif len(str)<2:
#     print("Only one str")
# else:
#     print(str[1::2])


# 5. Write a Python program that prints the string s without the character at index n. lf the index n is out of range, print the string s intact. 
# If the string s is empty, print the string s intact (string="hello”,n=1, output="hllo”.

# s=input("Enter a string: ")
# n=int(input("Enter a index: "))
# i=n
# if len(s)==0:
#     print("Enpty string")
# elif i<len(s):
#     print(s[0:i]+s[i+1:])
# else:
#     print("n is out of range")



# 6)Write a Python program that prints the string s with the character curr_char replaced by the character new_char.curr_char and new_char are 
# variables that contain strings with a single character.You may assume that new_char will not be an empty string.The match must be case-sensitive 
# (do not replace lowercase letters if curr_char is uppercase).If no match is found, print the initial string.
# (string=”hello” curr_char=”l”, new_char=”s”, output=”Hesso”

# str=input("Enter a string: ")
# cur_str=input("Enter a cur_str: ")
# new_str=input("Enter a new_str: ")
# if len(str)==0:
#     print("Empty str")
# else:
#     print(str.replace(cur_str,new_str))

# 7)Write a Python program that reverses the individual words in the string s and changes their capitalization. Uppercase letters should be 
# printed in lowercase and vice versa.
# •	Assume that the string only contains letters and spaces are used to separate words.

# word=input("Enter a string: ")
# new_word=""
# for i in range (len(word)):
#     if word[i].isupper():
#         new_word+=word[i].lower()
#     elif word[i].islower():
#         new_word+=word[i].upper()
#     else:
#         new_word+=word[i]
# print(new_word[::-1])

# or 

# s="Hello Word"
# s=input("Enter a text: ")
# word_list=s.split(" ")
# new_str=""
# for word in word_list:
#     revers_word="".join(reversed(word))
#     swapped_word=revers_word.swapcase()
#     new_str=new_str+swapped_word+ " "
# new_str=new_str.rstrip()
# print(new_str)

        

# 8)Write a Python program to convert a string s to lowercase, sort the characters of each word in alphabetical order, and print the resulting string.
# •	You may assume that the string only contains letters and spaces to separate the words.
# •	Spaces should be preserved in the final string.
#  String					Output
# “Hello World”			    “ehllo dlorw”
# “Wonderful World”			“defnoruw dlorw
# Hints:
# •	In Python, uppercase letters come before lowercase letters in alphabetical order.
# •	The sorted() function can be used to get a sorted list with the characters in a string.

# word=input("Enter a string: ")
# output=word.split(" ")
# new_word=""
# for i in range (len(word)):
#     if word[i].isupper():
#         new_word+=word[i].lower()
#     else:
#         new_word+=word[i]
#     output="".join(sorted(new_word))+" "
# print(output)

# or

# s=input("Enter a text: ")
# word_list=s.split(" ")
# new_str=""
# for word in word_list:
#     revers_word="".join(sorted(word))
#     swapped_word=revers_word.lower()

#     new_str=new_str+swapped_word+ " "
# new_str=new_str.rstrip()
# print(new_str)


