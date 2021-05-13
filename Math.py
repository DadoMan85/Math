
# Python3 DGallaway 4-28-21 Revision Date:

import random
import math


def main():
    print("Math Machine\n")

    choice = 0

    while choice != 4:

        print("1. Add 2 numbers")
        print("2. Multiply 2 numbers")
        print("3. Tip calculator")
        print("4. Exit")

        choice = int(input("Pick a number: \n"))

        if choice == 1:
            print("give me 2 numbers and I can add them together!\n")
            num1 = int(input("The first number is?: \n"))
            num2 = int(input("The second number is?: \n"))

            sum1 = num1 + num2
            print(str(num1) + " plus " + str(num2) + " equals " + str(sum1) + "!!\n")

        elif choice == 2:
            print("Welcome to the multiplication game!\n")
            print("give me 2 numbers and I can multiply them together!\n")
            num3 = int(input("The first number is?: \n"))
            num4 = int(input("The second number is?: \n"))

            sum2 = num3 * num4
            print(str(num3) + " times " + str(num4) + " equals " + str(sum2) + "!!\n")

        elif choice == 3:
            print("\nTip Calculator\n")
            num5 = float(input("Cost of the meal: "))
            print()
            num6 = num5 * .20 + num5
            print("The cost of your meal plus tip is: " + str(num6))

        elif choice == 4:
            print("Thank you, Goodbye!")

        else:
            print("Error, pick from the menu!\n")




if __name__ == "__main__":
    main()
