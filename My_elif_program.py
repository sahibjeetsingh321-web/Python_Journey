try:
    num= int(input("Enter the value of number:"))
    if (num<0):
        print("The number is negative.")
    elif(num==0):
        print("The number is zero.")
    elif(num==1313):
     print("The number is special.")
    else:
     print("The number is positive.")

except ValueError:
    print("Invalid number. Sahi number try karo.")

#Input wale case ch:
# try-except concept odo use karna hunda jado apa chahunde ha ki program end ho je jekar user ne koi hor input ditti hai. 
