
'''
    Alhassan Abdulmutallib
    
    This program take inputs of integer vals and compare, then present lagest num 
'''

import math

def checkMaximum(first,second):

    #Checking if the First Input is Highest
    if first> second:

    #Checking if the Second Input is Highest
        return first

    #Comparing the two inputs
    elif second>first:
	#if Not, program will return number
        return second
    else:
	#If result match the same input, then 0 returns
        return 0

#Getting Input from User
firstNumber = int(input("Enter the first number to Compute: "))
secondNumber = int(input("Enter the second number: "))

#Injecting the function that holds the values
highest = max(firstNumber,secondNumber)

#When the result is zero, it means, the input are the same
if highest == 0:
    print("Both numbers are the same")
else:
    #This part return the lagest val
    print(str(highest) + " is the largest number")

