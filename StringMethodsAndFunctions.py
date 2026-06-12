# Strings are immutable
# python ch eh hai ki variable name ikk sticker vangu hai matlab ki eh name apa kise hor value nu vi de sakde ha par hairani wali gall hai ki dono values de variable name same hon de bawjood vi output independent rahu.
a = "!!!Sahib!! !!!!!! Sahib!!"
print(len(a))
print(a)
print(a.upper())  # Eh function original string nu change (mute) nahi karuga par usdi copy banake print kar du.

print(a.lower())

print(a.rstrip("!"))  #String de last wale portion de  slash sign nu remove kardu.


print(a.replace("Sahib", "Singh"))
print(a.split("  "))  # Jekar string ch spacing ditti hove tan usde base te string nu split karda.

blogHeading = "introduction tO JavaScript"
print(
    blogHeading.capitalize()
)  # Line de pehle akhar 'i' nu captalize karke usi line de baki sabh elements  nu sahi kardu jive 'o' , 'j' , 's'.

str1 = " Welcome to the Console!!!"
print(len(str1))
print(str1.center(50))  # String nu center align karda.
print(len(str1.center(50)))
print(
    a.count("Sahib")
)  # Eh string 'a' cho pata karu ki Sahib kinni vaar likheya?? Answer: 2

str1 = "Welcome to the Console!!!"
print(
    str1.endswith("!!")
)  # Eh true or false vich answer deyu ki apni string slash naal end ho rahi hai ki nahi. Is case ch answer true hai kyunki last de vich 2 slash present ne.

str1 = "Welcome to the Console!!!"
print(str1.endswith("to", 4, 10))# Jekar 'to' index 10 te khatam ho reha ta answer true au, else false.

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))# Output is 10. Index start from 0 te dassda ki index 10 te 'is' peya. Jekar 'is' na hove ta -1 return karda.

print(str1.index("is"))# find() di tarah hi kamm karda, farak sirf ena ku aa ki jekar 'is' na hoya ta error show karu te program crash kardu matlab usto agge da program interpreter nahi read karu te nahi output do.

str1 = "1Welcome to the Console!!!"
print(str1.isalnum())# Jekar string ch spacing hove ya symbols ta sidha answer false au.
str1 = "1Welcome"
print(str1.isalnum())#Jekar koi digit na vi hove ta vi output true aundi hai bas alphabet hona chahida jekar alpha na hove ta digit hona chahida matlab string khaali nahi honi chahidi.. Jekar koi symbol use kita ta answer false au....  

str1 = "Welcome"
print(str1.isalpha())# Jekar digit aa gya ta answer false.

str1 = 'We wish you Happy Gurpurab'
print(str1.isprintable())# True

str1 = "hello world" #single quotes vi string layi use kar saakde aa par dujia languages ch error na hon islayi double quotes.
print(str1.islower())# True

str1="  " # using spacebar
print(str1.isspace())

str1 = "        " #using tab key
print(str1.isspace())

str1 ="World Health Organization"
print(str1.istitle()) # Jekar harek akhar da pehla akhar wadda ta true show karu, else false.

str2 ="To Kill a Mocking Bird"
print(str2.istitle())

str1 = "Python is an interpreted language."
print(str1.startswith("Python"))

str1 = "Python is an interpreted language."
print(str1.swapcase()) # jehde vi akhar chhote case ch ne oh vdde ho jaange te jehde vi vadde ne oh chhote ho jaange.

str1 = "His name is Dan. He is an honest man."
print(str1.title())# Harek word de pehle akhar nu upper case ch change kardu.