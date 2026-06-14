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
   #ਪ੍ਰੋਗਰਾਮ 4 ਦਾ Word-by-Word ਪੋਸਟਮਾਰਟਮ
# ਆਪਾਂ ਇਸ ਕੋਡ ਦੀ ਹਰੇਕ ਲਾਈਨ ਨੂੰ ਕੰਪਿਊਟਰ ਦੇ ਦਿਮਾਗ ਵਾਂਗ ਪੜ੍ਹਦੇ ਹਾਂ:

# Python
# num = 0
# ਕੰਪਿਊਟਰ ਕਹਿੰਦਾ ਹੈ: ਠੀਕ ਹੈ, ਮੈਂ ਇੱਕ ਡੱਬਾ ਬਣਾ ਲਿਆ ਹੈ ਜਿਸਦਾ ਨਾਮ num ਹੈ ਅਤੇ ਉਸਦੇ ਅੰਦਰ 0 ਪਾ ਦਿੱਤਾ ਹੈ।

# Python
# while num < 10:
# ਕੰਪਿਊਟਰ ਕਹਿੰਦਾ ਹੈ: ਇਹ ਇੱਕ ਲੂਪ (ਗੇੜਾ) ਹੈ। ਮੈਂ ਇਹ ਗੇੜੇ ਉਦੋਂ ਤੱਕ ਲਾਉਣੇ ਹਨ ਜਦੋਂ ਤੱਕ ਡੱਬੇ (num) ਵਿਚਲਾ ਨੰਬਰ 10 ਤੋਂ ਛੋਟਾ ਹੈ। ਹਾਲੇ num 0 ਹੈ, ਤਾਂ ਚਲੋ ਅੰਦਰ ਚੱਲਦੇ ਹਾਂ!

# Python
#     num += 1
# ਕੰਪਿਊਟਰ ਕਹਿੰਦਾ ਹੈ: ਮੈਂ num ਵਿੱਚ 1 ਜੋੜ ਰਿਹਾ ਹਾਂ। ਹੁਣ num ਦੀ ਵੈਲਯੂ 1 ਹੋ ਗਈ ਹੈ। (ਪਹਿਲਾ ਗੇੜਾ)।

# Python
#     if num % 2 == 0:
#         continue 
# ਕੰਪਿਊਟਰ ਕਹਿੰਦਾ ਹੈ: ਕੀ num ਨੂੰ 2 ਨਾਲ ਵੰਡਣ 'ਤੇ ਬਾਕੀ (remainder) ਜ਼ੀਰੋ ਬਚਦਾ ਹੈ? ਯਾਨੀ ਕੀ ਇਹ Even ਨੰਬਰ (ਜੋਟਾ) ਹੈ?

# ਧਿਆਨ ਦਿਓ: ਜੇਕਰ num 2 ਹੈ, ਤਾਂ ਇਹ ਕੰਡੀਸ਼ਨ True ਹੋ ਜਾਵੇਗੀ। ਇੱਥੇ continue ਹੁਕਮ ਦੇਵੇਗਾ: "ਰੁਕ ਜਾਓ! ਇਸਤੋਂ ਥੱਲੇ ਵਾਲਾ ਕੋਈ ਵੀ ਕੋਡ ਨਾ ਪੜ੍ਹੋ। ਸਿੱਧਾ ਵਾਪਸ ਉੱਪਰ while ਲਾਈਨ 'ਤੇ ਛਾਲ ਮਾਰੋ ਅਤੇ ਅਗਲਾ ਨੰਬਰ ਸ਼ੁਰੂ ਕਰੋ।" ਇਸੇ ਕਰਕੇ Even ਨੰਬਰ ਕਦੇ ਪ੍ਰਿੰਟ ਹੀ ਨਹੀਂ ਹੁੰਦੇ।

# Python
#     if num == 7:
#         print("Found 7! Breaking the loop.")
#         break
# ਕੰਪਿਊਟਰ ਕਹਿੰਦਾ ਹੈ: ਕੀ num ਬਿਲਕੁਲ 7 ਦੇ ਬਰਾਬਰ ਹੈ? ਜੇ ਹਾਂ, ਤਾਂ ਸਕ੍ਰੀਨ 'ਤੇ ਮੈਸੇਜ ਦਿਖਾਓ ਅਤੇ break ਕਰ ਦਿਓ। break ਦਾ ਮਤਲਬ ਹੈ ਕਿ ਭਾਵੇਂ ਲੂਪ ਨੇ 10 ਤੱਕ ਜਾਣਾ ਸੀ, ਪਰ ਹੁਣ ਇਸਨੂੰ ਵਿਚਾਲੇ ਹੀ ਤੋੜ ਕੇ ਬਾਹਰ ਆ ਜਾਓ।

# Python
#     print("Odd number:", num)
# ਕੰਪਿਊਟਰ ਕਹਿੰਦਾ ਹੈ: ਇਹ ਲਾਈਨ ਸਿਰਫ਼ ਉਦੋਂ ਹੀ ਚੱਲੇਗੀ ਜੇਕਰ ਉੱਪਰਲਾ continue (Even ਨੰਬਰ ਵਾਲਾ) ਨਹੀਂ ਚੱਲਿਆ। ਇਸਦਾ ਮਤਲਬ ਹੈ ਕਿ ਨੰਬਰ Odd (ਟਾਂਕ) ਹੈ, ਇਸ ਲਈ ਮੈਂ ਇਸਨੂੰ ਸਕ੍ਰੀਨ 'ਤੇ ਛਾਪ ਦਿੰਦਾ ਹਾਂ।

# 📝 ਅਸਲ ਵਿੱਚ ਸਕ੍ਰੀਨ 'ਤੇ ਕੀ ਹੋਵੇਗਾ? (Dry Run)
# num = 1: Even ਨਹੀਂ ਹੈ, 7 ਨਹੀਂ ਹੈ ➔ ਪ੍ਰਿੰਟ ਹੋਵੇਗਾ: Odd number: 1

# num = 2: Even ਹੈ ➔ continue ਚੱਲੇਗਾ ➔ ਥੱਲੇ ਵਾਲਾ ਕੋਡ ਇਗਨੋਰ, ਸਿੱਧਾ ਅਗਲਾ ਗੇੜਾ! (ਕੁਝ ਪ੍ਰਿੰਟ ਨਹੀਂ ਹੋਇਆ)

# num = 3: Even ਨਹੀਂ ਹੈ, 7 ਨਹੀਂ ਹੈ ➔ ਪ੍ਰਿੰਟ ਹੋਵੇਗਾ: Odd number: 3

# num = 4: Even ਹੈ ➔ continue ਚੱਲੇਗਾ ➔ ਸਿੱਧਾ ਅਗਲਾ ਗੇੜਾ!

# num = 5: Even ਨਹੀਂ ਹੈ, 7 ਨਹੀਂ ਹੈ ➔ ਪ੍ਰਿੰਟ ਹੋਵੇਗਾ: Odd number: 5

# num = 6: Even ਹੈ ➔ continue ਚੱਲੇਗਾ ➔ ਸਿੱਧਾ ਅਗਲਾ ਗੇੜਾ!

# num = 7: Even ਨਹੀਂ ਹੈ, ਪਰ ਇਹ 7 ਹੈ! ➔ break ਚੱਲੇਗਾ ➔ ਲੂਪ ਪੱਕੇ ਤੌਰ 'ਤੇ ਖਤਮ!

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

