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

def main():
    n = eval(input("Please enter a whole number for the factorial:")) #user input which factorial number
    fact  = 1 # fact is going to change when it goes through the loop
    for factor in range(n,1,-1): #produces a list starting with n and countig down but not including 1 as this will be 0. (1+0 - 1)
        fact = fact *factor
    print ("The facotrial of", n, "is", fact)
main()