# Counting vowels in a string
def count_vowels(string):  #string = "Hello world"
    count = 0
    vowels_letters = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for letter in string:
        if letter in vowels_letters:
            count += 1 #count = count + 1

    return count


def reverse_string(string):  #string = "Hello world"
    reversed_string = ''  #H

    for letter in string:
        reversed_string = letter + reversed_string   # e + H => eH

    return reversed_string


# eve => eve , since reverse of eve is same as eve it is a palindrome string
def is_palindrome(string):
    # if string == reverse_string(string):
    #     return True
    # else:
    #     return False
    return string == reverse_string(string)