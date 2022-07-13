list = [2,14,6,4,4,14,2,2,7,8,8,14]
print(" The original list : "+ str(list))

k=2
res =[]
for i in list:
    freq = list.count(i)
    if freq > k and i not in res:
        res.append(i)

print(" The required elements : "+ str(res))