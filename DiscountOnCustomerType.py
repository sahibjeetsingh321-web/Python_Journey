# Apa is program ch eh problem solve kar rahe ha ki apa customer di type dekh ke discount devange.

customer_type= input("The customer type is:")

match customer_type: 
         case "New":
            print("20% Discount")# ethe jado mai % discount likh reha si ta akhar red ho gye si kyunki %d ikk special keyword hai.
         case "VIP":# hun ta case keyword match di identation de andr hai par jdo e bahar si tan identation error aa reha si.
            print("30% Discount")
         case _ :
            print("No discount")

