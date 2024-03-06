import math
#Define calculate_distance functions with 2 tuples C1 and C2 as Arguments
def calculate_distance(C1,C2):
#Declare local Variables and extract values from tuples
 localX1, localY1=C1
 localX2, localY2=C2 
#Math operation ab variables with Euclidean distance Formulae 
 d=math.sqrt(((localX1-localX2)**2)+((localY1-localY2)**2))
#Return the result 
 return d
#Heading for the Program
print("Euclidean distance Program")
#Initiating toRun Variable that tracks user input to exit the program
toRun=""

#Loop with condition to exit if the toRun value is exit
while toRun != "exit":
#Try Except block to check if the entered Values are integers or floats
    try:
#Declare variables and get the input from user as Floats
      x1=float(input('Enter x1 co-ordinate:'))
      y1=float(input('Enter y1 co-ordinate:'))
      x2=float(input('Enter x2 co-ordinate:'))
      y2=float(input('Enter y2 co-ordinate:'))
#converting user input to Tuples to pass them as Arguments
      cordinateOne=(x1,y1)
      cordinateTwo=(x2,y2)

#Print result by Calling calculate_distance function and passing 2 tuple values as arguments    
      print ("The Euclidean distance for the co-ordinates",cordinateOne," AND ", cordinateTwo," is :",calculate_distance(cordinateOne,cordinateTwo))
#Option Input to user to either exit the program or Run it Again
      toRun=input('Enter "exit" to Exit the Program to run the program again press Enter')
#Except block to catch the exception and show the user the Custome error Message  
    except Exception as Argument:
#Cusotm Error Message
     print("Error you have to enter valid Numbers as Input Try Again\n", Argument)
