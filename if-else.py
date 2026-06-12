apple_Price= int(input("Bhai seb ki rate ne:"))
budget  = int(input("Enter your budget:"))
if (budget - apple_Price >= 50):
    print("Bhai ikk kilo Seb dede.")
    if(apple_Price<100):
        print("Bhai seb mehnge lade, mere kol bahut paise ne.")
    
else:
    print("Bhai seb bahut mehnge ne,na teri na meri, addhe rate lala,nahi  phir rehan de.")
