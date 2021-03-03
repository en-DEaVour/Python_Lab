#Name- MOHD MUSTAJAB KHAN
#En.No- A180570
#Roll No- 33
print("To find Year is a leap year or not")
while 1:
    try:
        year = input("Enter a year: ")
        year = int(year)
        if (year % 4) == 0:
            if (year % 100) == 0:
                if (year % 400) == 0:
                    print(year,"is a leap year")#For all 3 Condition's it print's
                else:
                    print(year,"is not a leap year")
            else:
                print(year,"is a leap year")
        else:
            print(year,"is not a leap year")
        break
    except ValueError:
        print("Enter number only")
        break
#year=int(input("Enter year to be checked: "))
#if(year%4==0 and year%100!=0 or year%400==0):
#    print("The year is a leap year!")
#else:
#    print("The year is not a leap year!")
