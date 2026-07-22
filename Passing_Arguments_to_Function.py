# Default arguments: Oh arguments jehdiya function create karde vele apa function de vich hi define kar dinde ha te jekar function call apa us parameter nu jekar koi argument dinde vi nahi ta vi koi error nahi aunda kyunki apa pehla hi function ch define karta si. Te jekar call karan vele us parameter nu navi value vi de sakde ha jis naal default di jagah navi value us parameter nu milju.


def name(fname, mname="Singh", lname="Khalsa"):
    print("Sat Sri Akaal,", fname, mname, lname,"Ji")


name("Gurmeet")
name(fname="Ram",mname="Krishan",lname="Pandit")#default values change kartiya. With the help of keyword arguments.
# Note: Required argument Jive 'Gurmeet'hai eh hamesha default arguments ton pehla hi aungia . iss case ch fname(parameter) ikk required argument lavega. jive apne function ch vi fname ikk required argument hai jis bina program nahi chall sakda te missing argument da error aunda hai. Te mname te lname ikk default argument ne je apa function call vele na vi koi argument devange ta vi koi chakkar nahi te jekar default value di jagah koi hor value(arguments) dena chahunde ha ta keyyword arguments devange.

# Keyword arguments: Oh jehdiyan apa call vele khud define karde ha te ethe order ya position change hon da chakkar nahi hunda.
def name(fname,mname,lname):
   print("Akaal!!!",fname,mname,lname,"Ji")
name(lname="Khalsa",mname="Singh",fname="Sher",)

# Required arguments:Jado apa key = value syntax nahi use kare ta eh zaruri ban jaanda ki apa ehna nu corrct position te correct amount ch deyiye. Correct amount to bhaav ki je function nu 3 arguments dene ne ta 3 hi dene painge. 

# Example 1: Jado number of argumnets(or values) passed doesn't match actual function definition.

def name(fname,mname,lname):
    print("Hello",fname,mname,lname,"Bro")

# name("Harry","Peter")# Value Harry will passed to fname(parameter) and Peter will passed to mname but no argument is pasesed to lname so there will be error of TypeError: name() missing 1 required positional argument: 'lname'

#Example with correct number of arguments passed:
def name(fname,mname,lname):
    print("Hello",fname,mname,lname,"Bro")

name("Harry","Peter","Quill")

#Variable - length arguments:
# Kayi vaar apa nu zyad argumentsa bhejan di lorh paindi hai ta apa eh kamm iss type de arguments bhejne painde ne.

# Eh kamm do ways naal hunda.
# 1. Arbitary arguments
# 2.Keyword arbitary arguments

# Arbitary arguments:
# function ch parameter de agge single star laga ke.

def name(*name):
    print("Akaal !!!",name[0],name[1],name[2],name[3])
#functions tuple di form ch process karke arguments nu access karda.
name("Nawab","Kapoor","Singh","Ji")
#Output:Akaal !!! Nawab Kapoor Singh Ji

# Keyword arbitary arguments:
# Function de Parameter to pehla double star laga ke. Iss case ch function arguments nu list di form ch process karke access karda. 
def name(**name):
    print("Akaal !!!",name['fname'],name['mname'],name['m2name'],name['lname'])
name(m2name='Singh',mname='Kapoor',fname='Nawab',lname='Ji')
# return statement bare apa padh hi leya si ki jekar kise varible nu function di value deni hove ta ap function ch return use karde ha. return asal ch calling function nu value return krda.
def name(fname, mname, lname):
    return "Hello, " , fname ," " , mname , " " , lname
#('Hello, ', 'James', ' ', 'Buchanan', ' ', 'Barnes')
print(name("James", "Buchanan", "Barnes"))


def name(fname, mname, lname):
    return "Hello, " + fname + " " + mname + " " + lname

print(name("James", "Buchanan", "Barnes"))
# Output :Hello, James Buchanan Barnes


# Rule 1 (The VIP Rule): Positional Arguments ਹਮੇਸ਼ਾ Keyword Arguments ਤੋਂ ਪਹਿਲਾਂ ਆਉਣਗੇ। (ਪਹਿਲਾਂ ਬਿਨਾਂ ਨਾਮ ਵਾਲੇ, ਫਿਰ ਨਾਮ ਵਾਲੇ)। matlab ki required arguments (non-default) hamesha pehla write karne ne.

# Rule 2 (The Default Rule): ਫੰਕਸ਼ਨ ਬਣਾਉਣ ਵੇਲੇ Default Arguments (ਜਿਵੇਂ name=Customer) ਹਮੇਸ਼ਾ ਨਾਨ-ਡਿਫੌਲਟ ਤੋਂ ਬਾਅਦ/ਅਖੀਰ ਵਿੱਚ ਲਿਖੇ ਜਾਣਗੇ।
# def profile(name="Customer", age):
#     print("Name:", name, "Age:", age)
# ਸਹੀ ਤਰੀਕਾ: def profile(age, name="Customer"):

# *args ਦਾ ਰਾਜ਼: ਇਹ ਸਾਰੀਆਂ ਵਾਧੂ positional ਵੈਲਯੂਜ਼ ਦਾ Tuple () ਬਣਾਉਂਦਾ ਹੈ। ਇਹ ਬਦਲਿਆ ਨਹੀਂ ਜਾ ਸਕਦਾ (Immutable)।

# **kwargs ਦਾ ਰਾਜ਼: ਇਹ ਸਾਰੀਆਂ ਵਾਧੂ keyword ਵੈਲਯੂਜ਼ (key=value) ਦੀ Dictionary {} ਬਣਾਉਂਦਾ ਹੈ।

# The Unpacking Trick: ਜੇ ਤੇਰੇ ਕੋਲ ਪਹਿਲਾਂ ਹੀ ਇੱਕ ਲਿਸਟ [1, 2, 3] ਹੈ ਅਤੇ ਤੂੰ ਉਸਨੂੰ *args ਵਾਲੇ ਫੰਕਸ਼ਨ ਵਿੱਚ ਭੇਜਣਾ ਹੈ, ਤਾਂ ਕਾਲ ਕਰਨ ਵੇਲੇ ਵੀ ਤਾਰਾ * ਲਗਾਉਣਾ ਪੈਂਦਾ ਹੈ: my_func(*my_list)।
#Example:
# Python
def count_items(*items):
    print(len(items))

clay_products = ["Clay Pot", "Kulhad", "Diya", "Handmade Plate"]
count_items(clay_products)

# Output one au , output   4 ave islayi
# Python
def count_items(*items):
    print(len(items))

clay_products = ["Clay Pot", "Kulhad", "Diya", "Handmade Plate"]
count_items(*clay_products)
