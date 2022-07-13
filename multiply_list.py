list1 = [12,5,34]
list2 =[3,6,7]

multiplied = list()
for item1,item2 in zip(list1,list2):
    item = item1 * item2
    multiplied.append(item)

print(multiplied)