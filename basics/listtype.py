lst=[10,20,"chetan",20.9]
print(lst)
print(len(lst))
print(lst*4)
print(lst[2])
print(lst[0:2])

lst.append(40)
lst.append("babu")
lst.remove("chetan")
lst.append("chetan")
del(lst[2])
print(lst)
print(lst*2)
print(len(lst))

print(lst)
#print(max(lst))
#print(min(lst))
lst=[10,20,55,99,20.9]
print(lst)
print(max(lst))
print(min(lst))
lst.sort()
print(lst)
lst.sort(reverse=False)
print(lst)
print(len(lst))
print(lst*4)
print(lst[2:5])
