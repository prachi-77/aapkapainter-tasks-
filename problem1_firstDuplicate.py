



def find_firstDuplicate(x):
    temp_arr=[]
    first_dupl_elem=None
    for i in x:
        if i not in  temp_arr:
            temp_arr.append(i)
        else:
            first_dupl_elem=i
            break
    return first_dupl_elem


print(find_firstDuplicate([1,2,3,2,1]))

