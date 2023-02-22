import random
import sys

def main():
    option = input("Roll the dice (yes or no): ").upper()
    if option in ["YES", "Y"]:
        dice_rolling()
    elif option in ["NO", "N"]:
        sys.exit("Exit")
    else:
        sys.exit("Invalied input")

def dice_rolling():
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    print(f"Dice rolled {dice_1}:{dice_2}")
    option = input("Roll again (yes or no): ").upper()
    if option in ["YES", "Y"]:
        dice_rolling()
    elif option in ["NO", "N"]:
        sys.exit("Exit")
    else:
        sys.exit("Invalied input")

main()