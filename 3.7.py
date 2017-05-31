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
    print("This program caclulates thedistance of a line through 2 pointts entered by the user")
    x1,y1 = eval(input("Please enter the coordinates (x1,y1)"))
    x2,y2 = eval(input("Please enter the coordinates (x2,y2)"))
    equation= (y2 - y1) ** 2 + (x2 - x1) ** 2
    distance = math.sqrt (equation)
    print("The distance of line through the cooridnates in the plane is:", round(distance,2))

main()