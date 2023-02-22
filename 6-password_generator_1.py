import string
import random
import sys

def main():
    option = input("Do you want to generate password (yes or no): ").upper()
    if option in ["YES", "Y"]:
        length = int(input("The length of the password that you want to generate: "))
        print(password_generator(length))
    elif option in ["NO", "N"]:
        sys.exit("Exit")
    else:
        print("Invalid input")


# Use the (random.sample) function when you want to choose multiple random items from a list without including the duplicates.
# Use (random.choices) function when you want to choose multiple items out of a list including repeated.
# (random.shuffle) This method changes the original list, it does not return a new list.
def password_generator(len):
    characters = string.ascii_letters + string.punctuation + string.digits
    list = random.sample(characters, len)
    random.shuffle(list)
    password = "".join(list)
    return password

main()
