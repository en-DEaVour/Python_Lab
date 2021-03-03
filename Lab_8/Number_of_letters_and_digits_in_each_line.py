#Name- MOHD MUSTAJAB 
#Roll no- 33
#EN no- A180570
f = open("mk123.txt","r")
f = f.readline()#TO read line by line      #if U use f.read ->
Digits=Alphabets=0                         #Then it can read whole character's and numeric 
for c in f:
    if c.isdigit():
        Digits=Digits+1 
    elif c.isalpha():
        Alphabets=Alphabets+1
    else:
        pass
print("Letters", Alphabets) 
print("Digits", Digits)
