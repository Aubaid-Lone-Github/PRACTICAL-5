list1 = [9,78,140]
list2 =[4,67,89]

subtracted = list()
for item1,item2 in zip(list1,list2):
    item = item1 - item2
    subtracted.append(item)

print(subtracted)