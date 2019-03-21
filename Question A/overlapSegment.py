'''
    Alhassan Abdulmutallib

    This module define the liness of the x-axis
    to get the string input
'''


def convergent(lineOne, lineTwo):

    return list(set(lineOne) & set(lineTwo))
 
 #This takes the list of the entry keeping it to the end of the function
def main():
    entry1 = []
    entry2 = []

    #Acception input of overlapping vals
    input1 = int(input("Please, Enter First Line to test Overlapping: "))
    input2 = int(input("Enter the Second Line for the Overlapping Test: \n"))
    
    #First elements to compare
    print("Getting the List of First Entry \n")
    for x in range(0,input1):
        rangeInput=int(input("Enter Number for Intersection \n" + str(x+1) + ":"))
        entry1.append(rangeInput)
    #Second elements to compare
    print("Getting the List of Second Entry \n")
    for x in range(0,input2):

        #Getting an integer values or comaparison
        rangeInput=int(input("Enter Number for Intersection \n" + str(x+1) + ":"))
        entry1.append(rangeInput)
    
    print(" +++++++++++++++++++++   Result for Number Intersection ++++++++++++++++++++++ \n")
    print(" +++++++++++++++++++++   ############################## ++++++++++++++++++++++")
    #End results of the accepted inputs 
    print(" Point of Convergent {}, First Entry Intersection {} and Second  {} \n", convergent(entry1, entry2))
    print(" +++++++++++++++++++++   Result for Number Intersection ++++++++++++++++++++++")
    
main()