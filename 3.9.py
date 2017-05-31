#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     19/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    print("Write a program to calculate the area of a triangle")
    a,b,c = eval(input("Please enter the length the 3 sides in cm (a,b,c)"))
    s = (a+b+c) / 2
    a = ((s*(s-a)) * (s-b) * (s-c))
    area = math.sqrt(a)
    print("The area of this triangle is", round(area,2), "cm2")
main()