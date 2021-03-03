#Name- MOHD MUSTAJAB KHAN
#Roll No:- 33
#En No:- A180570
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
print("The given list is-:",list)
def list_slice(S, step):
    list=[]
    for i in range(3):
     list.append(S[i::step])                    
    return list                                # another approach 
print("List after changing position-:")        # uncomment below code to see the action
print(list_slice(list,3))                      # return [S[i::step] for i in range(step)]
    

 
"""C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
def list_slice(S, step):
    return [S[i::step] for i in range(step)]
print(list_slice(C,3))"""
