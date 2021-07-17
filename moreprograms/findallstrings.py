s ="take up one ideas and make that ideas your life."\
"think and dream of that ideas and leave every other ideas alone"
subs ="idea"
pos =-1
found = False
length =len(s)
while True:
    pos =s.find(subs,pos+1,length)
    if pos == -1:
        break
    print("found the sub string position:",pos)
    found = True
if found == False:
    print("sub string is not found")
