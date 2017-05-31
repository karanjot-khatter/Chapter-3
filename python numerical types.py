#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     17/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    print(round(math.pi,2)) #2 decimal places, change to 3 for 3 decimal places - in corportate maths function
    print(math.pi) #pi 3.14...
    print(math.sqrt(2)) #sqrt of 2
    print(int(4.5)) # does not round = 4.
    print(float(5)) # put decimal
    print(int("12")) # gives us interger 5.
    print(str(6.8)) #string
    print(type(3)) #class type
    print(11/4) #divison operator - always gives us a float
    print(11//4) #gives us an interger - doesn't round up / down.
    print(11%4) #gives us a remainder of interger divison
    print(abs(-3)) #positive value of number
    print(abs(3)) #positive value of number
    print(pow(2,3)) #powers same as ** (squares)
    print(pow(4,0.5)) #square root.. mixing int and float so answer float.

main()