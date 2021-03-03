#Program name-GREATEST NO.
#Name- MOHD MUSTAJAB KHAN
#En.No- A180570
#Roll No- 33
while 1:
        try:
                a=input("Enter the value of 'a'")
                b=input("Enter the value of 'b'")
                c=input("Enter the value of 'c'")
                a = int(a)
                b = int(b)
                c = int(c)
                if(a>b and a>c):
                    print("Value of a is Greatest i.e",a,)
                    break
                elif(b>a and b>c):
                    print("Value of b is Greatest i.e",b,)
                    break
                elif(c>a and c>b):
                    print("Value of c is Greatest i.e",c,)
                    break
                elif(a==b==c):
                    print(a,"=",b,"=",c,)
                    break
                else:
                    print("Not lie in the given Condition's")
                    break
        except ValueError:
                print(" Enter the value of a,b,c in Numeric Only")
                continue
    

  
  
