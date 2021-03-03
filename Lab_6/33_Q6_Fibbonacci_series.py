#Name- MOHD MUSTAJAB KHAN
#En.No- A180570
#Roll No- 33
a = -1
b = 1
print("For Fibbonacci series")
while 1:
    try:
        terms = input("Enter no of terms U want-: ")
        terms = int(terms)
        print("The Fibbonacci series formed is-:")
        for i in range(terms):
            c = a+b
            print(c)
            a = b 
            b = c 
        break
    except ValueError:
        print("Enter number only")
        break
