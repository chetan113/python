import sys

choicelist=sys.argv

accbalance=10000



choice=int(choicelist[1])

if(choice==1):

    print("your account balance =$",accbalance)

elif (choice==2):

    withdraw=int(input("Please enter the amount to be withdraw:  "))

if(withdraw<=accbalance):

    accbalnce=accbalance-withdraw

    print("Balance in your account is=$", accbalance)

else:

    print("Insufficient  balance in your account !" )

     elif(choice == 3):

        deposit=int(input(" please enter the  Amount to be Deposited: ")

    deposit=deposit+accbalance

    print("Amount in the account is: ", accbalance)

else:

    print("wrong choice. please choose the correct choice available ")