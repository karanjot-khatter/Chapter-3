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

def main():
    print("This program computes the nth fibonacci number where n is a value input by the user")
    n= eval(input("Please enter the nth value"))

    total = round(n/2)
    x,y =1,1
    fi = list([1,1]) #starting list of 1,1 ... then follow sequence.. 1,1,2,3,5,8

    for i in range(total):
        x = x+y
        fi.append(x) # add x end of list
        y = y+x
        fi.append(y) #add y end of list

    print(fi[n-1]) #from the list, pick nth number - 1
main()