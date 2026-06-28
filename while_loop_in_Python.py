#In while loop we have to initialize the variable like in C. In python there is no do-while loop so In py. we have to learn how to use while as do- while.
#Reverse calculation
# count=int(input("Enter the number:" ))# Variable initialization
# while count > 0:
#     print(count)
#     count-=1
#Guess the Secret Word
# secret_word="Python"
# guess=""#Variable initialization

# while guess != secret_word:
#     guess=input("Enter the secret word to escape the loop:")
#     if guess!= secret_word:
#         print("Wrong guess, try again!\n")
# print(f"Correct! The secret word was indeed'{secret_word}'.You are out of the loop now!!!!")
#Simulating do-whle loop in Python
print("~~~Welcome to the menu~~~ ")

while True:#Now this loop is start for always like a do-while loop.
    print("1.Play game.")
    print("2.Exit")
    choice=input("Enter your choice( 1 or 2):")
    if choice == "2":#Used quotations because input was a string.
        print("Exiing the menu.GoodBye!!")
        break# Eh loop nu zabardasti naal tod devega.
    else:
        print("Enjoy the game!!!")

#Skip even numbers and stop at 11

num = 0

while num< 10:
    num += 1

    if num%2 == 0:
       continue# Je number eve hai ta thalle wala code chhado te dubara loop ch jau te one plus ho ke odd number ban ju te thalle wala code run hou.
    if num == 7:
        print('7 is found!!Breaking the loop.')
        break
    print("Odd number:",num)
   
# ਸਿੱਟਾ: continue ਸਿਰਫ਼ ਇੱਕ ਖਰਾਬ ਗੋਲਗੱਪੇ ਨੂੰ ਛੱਡਦਾ ਹੈ, ਜਦਕਿ break ਗੋਲਗੱਪਿਆਂ ਦੀ ਰੇਹੜੀ ਤੋਂ ਹੀ ਘਰ ਵਾਪਸ ਭੇਜ ਦਿੰਦਾ ਹੈ!
i=0
Choosed_Number=int(input("Enter the number here at which you want to stop the counting:"))
while i<= Choosed_Number:
    print(i)
    i+=1 #i+1

i = int(input("Enter the number: "))# Is case ch apa while nu do-while di tarah use kita ode nu repeat karke par professionally jithe 2000 lines of code hon othe apa apne code nu 4000 lines of code nahi banavange. Othe apa break te continue da concept vartange.
print(i)
while(i<=38):
  i = int(input("Enter the number: "))
  print(i)

print("Done with the loop")

