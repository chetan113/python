"""s =input("enter a string:")
print(s[::-1])
"""

"""palendrom"""

"""
s= input("enter a string:")
i= len(s)-1
result = ''
while i>=0:
    result =result+s[i]
    i=i-1
print(result)
"""
""" join the string use reverse"""

s='---'.join(['a','b','c'])
print(s)


s1=input("enter a string:")
print(','.join(reversed(s1)))
