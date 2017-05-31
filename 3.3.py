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

def main():
    print("This program determines the moleculae weifght of a hydocarbon based on the number of hydrogen, carbon and oxygen atoms")
    h,c,o = eval(input("Please enter the total amount of Hydrogen atoms, Carbon atoms, Oxygen atoms (h,c,o):"))
    hydrogen = 1.0079 * h
    carbon = 12.011 * c
    oxygen = 15.994 * o
    total = hydrogen + carbon + oxygen
    print("The total weight of a hydrocarbon is", total)
main()