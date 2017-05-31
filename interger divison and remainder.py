#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Karanjot
#
# Created:     17/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    children = 3
    sweets = 14
    sweetsEach = sweets //children
    sweetsLeftForMe = sweets % children
    print(sweetsEach) #divison no round
    print(sweetsLeftForMe) #remainder
main()
