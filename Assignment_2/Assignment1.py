# Importing math module
import math
# Creating a function named integers
def integers():
    i=0
# Creating an empty list    
    list1=[]
    for i in range(10):
        try:
            # Appending integers into the list
            b=int(input("Enter the number"))
            list1.append(b)
        except ValueError:
            return ("Enter only integers")
    # Elements in the list
    print("You have entered the following elements ",(list1))
    # Maximum element in the list
    print("Maximum number in the list is {}".format(max(list1)))
    # Minimu element in the list
    print("Minimum nuber in the list is {}".format(min(list1)))
    # Range of elements in the list
    print("range of entered numbers is ",max(list1)-min(list1))
    c=sum(list1)/len(list1)
    print("Mean =",c)
    sum1=0
    # Calculating the sum of square of difference between the mean and elements in the list
    for i in range(len(list1)):
          sum1=pow((list1[i]-c),2)+sum1
    #Varience
    print("varience = {}".format(sum1/len(list1)))
    # Standard Deviation
    print("Standard Deviation = ",math.sqrt(sum1))
    
    