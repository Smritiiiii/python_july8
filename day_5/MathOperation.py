while (True):

    num_1= (float(input("enter 1st number"))) 
    num_2= (float(input("enter second number")))
    choice= int (input("enter the choice of operation 1.ADD  2.Sub  3.Multiply  4.Divide"))

    if (choice == 1):
        result= num_1+num_2
        print(result)
    elif(choice ==2):
        result= num_1-num_2
        print(result)
    elif(choice == 3 ):
        result= num_1*num_2
        print(result)
    elif(choice == 4):
        result = num_1/num_2
        print(result)

    else:
        print("enter the valid option")

    again = (input("do you want to continue?(Y/N)"))

    if (again=="N"):
        break
