import sys
from mine import get_int

def main():
    choice = None
    while not choice in ["A", "B", "C", "D", "E"]:
        print("A. Addition")
        print("B. Subtraction")
        print("C. Multiplication")
        print("D. Division")
        print("E. Exit")
        choice = input("Chose: ").upper().strip()

    if choice == "E":
        sys.exit()

    x = get_int("x: ")
    y = get_int("y: ")

    if choice == "A":
        print(add(x, y))
    elif choice == "B":
        print(sub(x, y))
    elif choice == "C":
        print(mul(x, y))
    elif choice == "D":
        print(div(x, y))
    
        


def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

main()