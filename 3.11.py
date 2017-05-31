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
    print("This program is used to find the sum of the first n natural numbers")
    n = eval(input("Please enter any natural value:"))
    sum = 0
    for i in range(n):
        sum = sum + 1
    print(sum)
main()