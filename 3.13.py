#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     20/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    print("This program is to sum a series of numbers entered by the user")
    numbers = eval(input("How many numbers are to be summed"))
    sum = 0
    for i in range(numbers):
        i = eval(input("Please enter a number: "))
        sum = sum + i

    print(sum)


main()