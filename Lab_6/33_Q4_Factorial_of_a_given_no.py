#Name- MOHD MUSTAJAB KHAN
#En.No- A180570
#Roll No- 33
print("To find factorial of a given number")
factorial = 1
while 1:
    try:
        num = input("Enter a number you want-: ")
        num = int(num)   
        if num < 0:
           print("Sorry, factorial does not exist for negative numbers")
        elif num == 0:
           print("The factorial of 0 is 1")
        else:
           for i in range(1,num + 1):
               factorial = factorial*i
           print("The factorial of",num,"is",factorial)
           break
    except ValueError:
        print("Enter number only")
        continue
#import math
#n = int(input("Enter the no U want"))
#print("The factorial of a given no is ",math.factorial(n))    
