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
    print("Program calculates thec ost per square inch of a circular pizza")
    diameter = eval(input("Please enter the diamaeter of the pizza (in meters)"))
    price = eval(input("Please enter the price of the pizza? (in pounds"))
    radius = diameter / 2
    area = math.pi * (radius ** 2)
    costPerInch = price / area
    print ("The cost per Inch of a circular pizza is:", round(costPerInch,3))

main()