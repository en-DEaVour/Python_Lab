# Name:- MOHD MUSTAJAB KHAN
# Roll no:- 33
# En. no:- A180570
def first_check_range():
    if( Input_no > 1000 and  Input_no < 2000):       # Range
        print("True")
    else:
        print("False")
while 1:
    try:
        Input_no= float(input("Enter any number and check that it comes under 1000 to 2000 or not :"))
        first_check_range()
        break
    except ValueError:
            print("Enter numeric only ")
            continue

