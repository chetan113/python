student={'chetan':["python","django","drf"],'babu':["java","spring"],'sakamuri':["sql","plsql"]}
keys= student.keys()
for eachkey in keys:
    print("course taken by",eachkey,"are")
    for eachcourse in student[eachkey]:
        print(eachcourse)
    