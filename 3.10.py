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
    print("Program to deterime the length of a ladder")
    height = eval(input("Please enter the height of the ladder? (m)"))
    angle = eval(input("Please enter the angle of the ladder (degrees)"))
    radians = (math.pi / 180) * angle
    length = height /math.sin (radians)
    print("The radians of the ladder is:", round(radians,3), ". The length of the ladder is:", round(length,2), "m")
main()
