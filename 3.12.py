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
    print("This program is to find the sum of the cubes of the first n natural numbers")
    n = eval(input("Please enter a natural number:"))
    sum = 0
    for i in range(n):
        sum = sum + (i**3) # change value of sum
    print(sum)
main()