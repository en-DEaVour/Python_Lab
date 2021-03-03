#Name- MOHD MUSTAJAB KHAN
#Roll no:- 33
#En No:- A180570
list = ([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
print("Given list is:-",list)
def last(n):
 return n[-1]
def list_which_we_have_to_sort(tuples):
  return sorted(tuples, key=last)
print("Now the sorted list in increasing order by the last element in each tuple is:-\n",list_which_we_have_to_sort([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
