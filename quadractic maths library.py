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

#A program that computes real roots ofa  quadratic equation
#Uses the maths library
#Note: This porgram crashses if the equation has no real roots
import math #Makes the maths library avaliable
def main():
    print("This program finds the real solutions to a quadratic")
    a,b,c = eval(input("Please enter the cofficents(a,b,c):")) # input to the program will be the values of coefficent a,b,c
    discRoot = math.sqrt(b * b - 4 *a * c) #everything in the squared equation
    root1 = (-b + discRoot) / (2*a) #who equation added
    root2= (-b - discRoot) / (2*a) # who equation minused
    print("The solutions are:", root1, root2) #outputs are the 2 values given by the quadratic formulae ( asks for minus and plus)
main()