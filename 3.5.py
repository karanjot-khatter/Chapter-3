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
    print("This program calculates the cost of an order")
    poundOfCoffee = eval(input("Please enter the amount of coffee (in pounds)"))
    coffee = 10.50 * poundOfCoffee
    shipping = (0.86 * poundOfCoffee) + 1.50
    totalCost = coffee + shipping
    print("From", poundOfCoffee, "pounds of coffee,the total cost of your order is: $",round(totalCost,2))

main()