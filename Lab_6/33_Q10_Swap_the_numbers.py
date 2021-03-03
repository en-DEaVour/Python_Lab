#Name- MOHD MUSTAJAB KHAN
#En.No- A180570
#Roll No- 33
print("Performing Swapping between two nos")
while 1:
    try:
        num1 = input('Enter First Number: ')
        num2 = input('Enter Second Number: ')
        num1 = int(num1)
        num2 = int(num2)
        print("Value of num1 before swapping: ", num1)
        print("Value of num2 before swapping: ", num2)
        temp = num1
        num1 = num2
        num2 = temp
        print("Value of num1 after swapping: ", num1)
        print("Value of num2 after swapping: ", num2)
        break
    except ValueError:
        print("Enter number only")
        break
