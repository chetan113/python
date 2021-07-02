dict1={1:"chetan",2:"babu",3:"sakamuri"}
print(dict1)

print(dict1.keys())
print(dict1.items())
print(dict1.values())

k=dict1.keys()
for i in k:print(i)

v=dict1.values()
for i in v:print(i)

del dict1[2]
print(dict1)

del dict1[3]
print(dict1)