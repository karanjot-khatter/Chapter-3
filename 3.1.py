#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     18/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    print("Program to claculate the volume and surface area of a sphere from its radius")
    radius = eval(input("What is the radius of the sphere?"))
    volume = 4 / (3 * math.pi * (pow(radius,3)))
    area = 4 * math.pi * (radius ** 2)
    print ("The volume of a sphere is:", round(volume,2))
    print ("The v Surface area of a sphere is:",  round(area,2))
main()