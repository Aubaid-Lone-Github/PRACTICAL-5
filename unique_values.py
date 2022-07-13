def unique(list):
    unique_list = []

    for x in list:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x,end=" ")        

list =[12,4,5,34,23,23,34,12,4,67]
print(" The unique values from list is ")
unique(list)