x=int(input("enter the min number:"))
y=int(input("enter the max number:"))

if x%2 == 0: x=x+1
while x<=y:
    print(x)
    x+=2