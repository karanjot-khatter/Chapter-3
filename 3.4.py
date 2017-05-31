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
    print("This program determines the distance of a lightning strike")
    timeInSeconds= eval(input("Please enter the time elapsed between the flash and the sound of thunder"))
    speedOfSound = 1100 / timeInSeconds
    distance = speedOfSound / 5280
    print("The distance to a lightning strike is:", round(distance * 1000, 2), "miles")

main()