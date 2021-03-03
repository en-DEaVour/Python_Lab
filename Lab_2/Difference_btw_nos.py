#Name- MOHD MUSTAJAB KHAN
#En.No- A180570
#Roll No- 33

#Question-You have to solve a Python program to get the difference between a given number
#(take input from the user) and 17, if the number is greater than 17 answers will be double the absolute difference"
while 1:
     try:
        input_no = float(input("Enter the number :"))
        if input_no>17 :
             Difference = (input_no-17)
             Result = Difference*2
             print("Result is ",Result)
             break
        else:
             Difference = (17-input_no)
             print("Result is ",Difference)
             break
     except ValueError:
            print("Enter numeric only")
            continue
