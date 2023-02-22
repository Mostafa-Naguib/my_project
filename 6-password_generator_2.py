import string
import random


def passowrd_generator(length, num=True, special_char=True):
    letters = string.ascii_letters
    numbers = string.digits
    special_chararcters = string.punctuation
    
    characters = letters
    if num:
        characters += numbers
    if special_char:
        characters += special_chararcters

    pwd = ""
    cretia = False
    # here we make sure that our password meet the cretia in special characters and num 
    while not cretia:
        # here we generate the password
        pwd = "".join(random.sample(characters, length))
        cretia = True
        # here we see if the password has at least one special character
        if special_char:
            for char in pwd:
                if char in special_chararcters:
                    cretia = True
                    break
                cretia = False
        # and here we see if the password has at least one number 
        if (num) and not (pwd.isalnum):
            cretia = False
    # and finally we shuffle the pwd before we return it
    return pwd


length = int(input("The length of your password: "))
has_number = input("Do you want numbers (Y/N): ").upper() == "Y"
has_special = input("Do you want special_characters (Y/N): ").upper() == "Y"
pwd = passowrd_generator(length, has_number, has_special)
print(pwd)
