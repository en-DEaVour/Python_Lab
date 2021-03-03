#Name- MOHD MUSTAJAB KHAN
#Roll no:- 33
#En No:- A180570
list =  [11, 33, 50]
print("Given list is-:",list)
print("To remove the spaces between the list's element")
while 1:
 try :
        print("PLEASE Press only 1:-")   
        a=int(input())
        if (a == 1):
            print("Now the list element's become-:")
            for i in list:
             print(i, end="")
            break;
 except ValueError:
            print("Wrong input")
            continue
