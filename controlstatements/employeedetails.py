n = int(input("enter the number of employes:"))
employees = {}
for i in range(n):
    name = input("enter employee name:")
    salary =input("enter the employee salary:")
    employees[name] = salary
while True:
        name= input("enter employee name")
        salary=employees.get(name,-1)
        if salary == -1:
            print("employee doesnt exist")
        else:
            print("the salary of the employee in:",salary)
        choice= input("do u want to know the salary of an other employes[yes/no]")
        if choice == 'no':
            break