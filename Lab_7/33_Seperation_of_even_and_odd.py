#Name- MOHD MUSTAJAB KHAN
#En.No- A180570
#Roll No- 33
f = open("integers.txt","r")
while True:
    line = f.readline()
    try:
        line = int(line)
        if line%2 == 0:
            f1 = open("evenInt.txt", "a")
            f1.write(str(line))
            f1.write("\n")
            f1.close()
        else:
            f2 = open("oddInt.txt","a")
            f2.write(str(line))
            f2.write("\n")
            f2.close()
        if not line:
            break
    except ValueError:
        break
print(f1.name)
print(f2.name)
f.close()
#After run the program go to the saved file folder and you find the two newly made file's i.e-: evenInt and oddInt
#open it and you find the seperate even nos and odd nos
