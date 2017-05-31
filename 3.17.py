#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     22/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    print("Program that implements newtons methods")
    value = eval(input("please enter the value to find the square root of x"))
    time= eval(input("Please enter the number of times to improve the guess"))
    time = time - 1
    guess = value / 2
    for i in range(time):
        guess = (guess + (value / guess)) / 2

    print("Your guess is",guess)

    real = math.sqrt(value)
    print("The real square root of", value, "is", real)
    difference = guess - real
    difference = 100 - (difference/real*100)
    print("The value is",int(difference),'% correct!')
main()