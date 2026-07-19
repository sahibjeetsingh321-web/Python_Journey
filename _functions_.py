# Functions da fayda : Jive apa kise app ch kise cheez nu like karan da code likh rahe ha jive reels ch like karan da ,videos nu like karan da te shorts nu like karan da ta apa code nu ehna 3 thaava te individually likhan di bajaye function bana ke ehna jagah te use karange.

# def calculateGmean(a,b):#Function name
#     mean = (a*b)/(a+b)# Function body
#     print(mean)

# def isGreater(a,b):
#     if(a>b):
#         print("First number is greater")
#     else:
#         print("Second number is greater")
# def isLesser(a,b):
#     pass#Jekar apan pass nahi likhange ta error au. Reason: Apa function name ta define kart par function body nahi. Jado apa vehle hovange ta pass keyword hta ke logic likh devange. par jado vi apa eda karna hove ta print statement ch '''To do later''' likh dena chahida ta jo apa baad ch us te kamm kar skiye.

# #   C language wangu sab to thalle code likhan layi ikk wakhri approach hundi hai, with the help of creating main fuction

# a=int(input("Enter the value of first number:"))
# b=int(input("Enter the value of second number:" ))

# isGreater(a,b)# Call karan layi semicolon use karan di lod nahi.
# calculateGmean(a,b)
# c= int(input("Enter the value of third number:"))
# d=int(input("Enter the value of fourth number:"))
# isGreater(c,d)
# calculateGmean(c,d)
# #Jekar functions na hunde ta gmean vale te is greater wala logic a,b te c,d layi dubara likhna painda.
# # Enforced Syntax Rules (Strict)
# # If you violate these rules, Python will throw a SyntaxError.Allowed Characters: Use only letters (A-Z, a-z), digits (0-9), and underscores (_).
# # No Leading Digits: A name cannot start with a number.
# # No Spaces or Symbols: Special characters (like -, @, $, %) and spaces are strictly forbidden.
# # Reserved Keywords: Do not use built-in keywords (such as if, else, while, def, class).
# # Case Sensitivity: Lowercase and uppercase letters are unique. user_age, User_Age, and USER_AGE are three different variables.
# # Eh rules jithe naming of variables layi ne othe naming of functions ch vi follow hunde ne.
# #Extra knowledge:
# # de fkeyword memory booking da kamm karda hai , python def nu dekh ke code nahin chala sakda kyunki eh sirf function create karke memory vh store karda jado apa call karange ta python us memory nu use karu.

# #paranthesis to bina kade vi function execute nai hunda jado apa function nu call karna hunda.


# # parameter vs  argument:
# def add(x,y):
#     print("The addition is:",x+y,)
# e=5
# f=6
# add(e,f)
#x,y parameters bhav khalibartan ne and e te f arguments bhav oh dabbe ch pain wala saman n.
#Jekar apa koi function do arguments lain wala banaya ta kade vi apa osnu three arguments nahi pass kar sakde nahi ta error au.

# 
# Execution flow:
# Interpreter top to bottom flow karda hai te function de andar udo enter hunda jado usnu call kita janda.
# inside-outside evaluation :jekar function de andar function call ho reha tan   andarla function pehla solve ya execute hunda.
#Example:display(max(10,20))
# ithe max() ikk built-in function hai jo greatest number dassda te display apa banaya jehde naal apa kise chhez nu print karange. Output ch 20 print hou.
#pass keyword di help naal apa funcion khali chhad sakde ha jis naal koi vi identation error nahi avega.

#print vs return:
#jekar function ch print likheya ta screen te ta oh cheez show ho ju par return kujh nahi hona.

# def addition_with_print(a,b):
#     print(a+b)

# def addition_with_return(a,b):
#     return a+b
# #Result nu  variables ch store karange
# ##variable_1=addition_with_print(5,5) 
# # print(variable_1) #Output-None
# # 'Will print 10  due tofunction call but jado variable 1 nu print karan di vaari au ta none show hou kyunki function returns nothing to variable 1'
# variable_2=addition_with_return(5,5)# value=10, variable 2 nu de devega.Jis nal variable nu iss value de naal baad ch use kar sakde ha.
# print(variable_2)#will print 10



# # function ikk data type ya object hai jo ki <class 'function' return karda.

 #Jekar apa kise function da name built_in function de name te rakh ditta ta uda work apne dura likhe hoye logic rahi hou na ki oh apne asal logic waangu kamm karu so kade vi eh mistake nahi karni. Phenomenon is called shadowing.

