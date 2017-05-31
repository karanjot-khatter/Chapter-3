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

def main():
    print("This program caclulates the gregorian epact - Value used to figure out the date of easter")
    year = eval(input("Please enter a 4 digit year"))
    C = year // 100 #gives us an interger - doesn't round up / down.
    epact = (8+(C//4) - C +((8 * C + 13) //25) + 11* (year % 19)) % 30
    print("The gregorian epact",epact, "days before January 1st")
main()