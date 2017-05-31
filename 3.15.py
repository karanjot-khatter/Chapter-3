#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Karanjot
#
# Created:     20/04/2017
# Copyright:   (c) Karanjot 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import math
def main():
    print("Proigram that approximates the value of pi")
    print('(4/1-4/3)+(4/5-4/7)+(4/9-4/11)+...')
    numbers= eval(input("Please enter the numbers of terms to sum"))
    sum = 0
    for i in range(numbers):
        sum = sum + 4.0 * (-1) ** i /(2* i + 1)
        accuracy = abs(math.pi - sum)/sum * 100
    print( "The approximation of pi with", numbers, "terms is", round(sum,2))
    print("The accuracy of this approximation is", round(accuracy,2), "%.")
main()