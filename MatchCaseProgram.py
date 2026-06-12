x = int(input("Enter the value of x:"))
# x, match keyword layi variable hai or x is the variable to match

match x:
    case 0:
        print("Value of x is 0")
    case 4:
        print("The case is 4.")
    case _ if x!= 90 and x< 100 :# case te if keyword de vichale jo dash hai isnu hamesha dono words to spacing de ke rakhni hai nahi ta red line show hou te interpreter socho ki case da name _if hai balki apa usnu eh dassna hai ki eh empty case statemnt hai.
        print(x, "is not equals to 90.")
    case _ if x!= 80 and x<100:
        print( x, "is not equals to 80.")
    case _ :# default case statement
        print(x)