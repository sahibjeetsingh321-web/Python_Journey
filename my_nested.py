num = int(input("ENTER THE NUMBER:"))
if(num<0):
    print("Number is negative.")
elif(num>0):
    if(num<=10):
        print("The number is between 1 to 10 ")
    elif(num>10 and num<=20):
        print("The number is between 11 to 20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")