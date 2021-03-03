#Name- MOHD MUSTAJAB KHAN
#Roll no:- 33
#En.No:- A180570
list=[1,2,3], [4,5,6], [10,11,12], [7,8,9]
print("Given list is-:",list)
sum1=0
for w in list[0]:
 sum1 += w
print("Sum of list[0]-:",sum1)
sum2=0
for x in list[1]:
 sum2 += x
print("Sum of list[1]-:",sum2)
sum3=0
for y in list[2]:
 sum3 += y
print("Sum of list[2]-:",sum3)
sum4=0
for z in list[3]:
 sum4 += z
print("Sum of list[3]-:",sum4)
if sum1>sum2 and sum1>sum3 and sum1>sum4:
 print("Sum of list[0] is maximum and the list is-:",list[0])
elif sum2>sum1 and sum2>sum3 and sum2>sum4:
 print("Sum of list[1] is maximum and the list is-:",list[1])
elif sum3>sum1 and sum3>sum2 and sum3>sum4:
 print("Sum of list[2] is maximum and the list is-:",list[2])
else:
 print("Sum of list[3] is maximum and the list is-:",list[3])


