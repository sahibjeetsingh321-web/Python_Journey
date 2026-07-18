# for i in range(12):#Apa 11 tak ginti print kara rahe ha.Loop i=11 takk challu.
#     if(i==10):
#         print("Skip the iteration")#5*10 layi print nahi hou.
#         continue
#     print("5 into",i,"is :",5*i)
# for i in range(12):
#     if(i==11):
#         print("Loop chadd ke chale jao.")
#         break
#Python de andar do-while loop use karan da tarika
# Step 1:variable initialization
# while True:#T capital chahidi hai
#     print(statement)
#     increment or decrement
#     if(oh condition jis de true hon te hi loop challni chahidi hai ):
#         break 
'''do while ikk exit contol loop hai te while entry control loop hai bhav ki jekar do-while de andar di condition false vi hove taa vi loop ik vaar challu.'''
i=0
while True:
    print("Singh is King")
    i=i+1
    if(i>=0):
        break

#do-while loop syntax in Python:
# while True:
#     block of code
#     increment or decrement
#     if-condition
#     break
# jekar apa while loop de andar break statement chala diye ta kade vi else block wala part ahi challda. else block odo challda jado loop naturally end hundi hai.
# kise vi loop statement ch increment ya decrement karna sab to zaruri hai nahi ta program ch error aunda hai.
#Revision sheet:
#jekar loop infinite ban gy hai ta heck karo ki increment ya decrement kita si kyunki je variable di value hi nahi change hou te condition true hi rahu ta loop infinite ban ju.
# break statement: poore de poore loop de block to bahar lai jandi hai.
i=0
while(i<=3):
    print(i)
    i=i+1
    if(i==2):
        break
else:
    print("else wali statement print nahi hui???")#else wali statement print nahi hoyi si bhavein ki of while di identation to bahar si.