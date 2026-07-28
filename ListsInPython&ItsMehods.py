# marks = [3,5,6,"Sahib",True,3.5,32,345,63]
# print(marks)
# print(marks[:])#Dono da matlab same hai.Baki eh cheez apa strings padhan vele vi kiti si ehnu slicing vi kehnde ne.
# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])
# for i in range(9):
#     print(marks[i])
    

# print(marks[-3]) #Negative index 
# print(marks[len(marks)-3]) # Positive index.Easy way to understand and print negative index
# print(marks[9-3]) #Positive index 
# print(marks[6]) #Positive index
# #Sab da matlab ikk hi hai.
# # Note: Loop hamesha index 0 to start hunda te in-1 times challda .Apni list ch 9 items si te loop apa index 8 takk chalwauna si ta ki 9 items print ho jaan islayi apa range de andar 9 likheya.

# # Note: Jekar kise list da last indx 8 hai ta usdi length 8 nahi hundi balki ikk vadh ke hu. Kehan da bhaav ki ength te index ch farak samjhna hunda.
# if 6 in marks:
#     print("Yes, item is in the list.")
# else:
#     print("Item is not in the list.")
# if "6" in marks:
#     print("Yes")
# else:
#     print("No")
# if "Sahib" in marks:
#     print("Yes")
# else:
#     print("No")

# # Same thing applies for string as well !!!!
# if "Sa" in 'Sahib':
#     print("Yes")
# else:
#     print('No')
# if"hil" in 'Sahib':
#     print('Yes')
# else:
#     print("No")
# list1 =[i*i for i in range(10)]
# print(list)
# list2=[i*i for i in range (101) if i%10==0]
# print(list2)
# list3=[i for i in range (101) if i%10==0]
# print(list3)
# #Eh  tarike koi khaas logic ya kujh khaas elements nu list ch bharan de hunde ne ta jo manually type na karna pave. 

# List methods:

list3 = [11,22,33,44,55,66,1,77,1,88,11]
print(list3)
list3.append(99)#List mutable hai islayi apa is ch changes kar sakde ha jive append da use karke nava element list ch addkar sakde ha par tuple ch eh poosible nahi.
list3.sort()
print(list3)

list3.sort(reverse=True)#Is naal apni list descending ordr ch sort ho ju.
print(list3)
#Note: Apa harek vaar list te function apply karke list nu mute bhav change karke print kar  rahe han jis to bhav hai ki list mutable hundi hai.
print(list3.index(1))#Output:10 Reaso:Apni list descending order ch sort ho gyi te index 10 te function nu sab to pehla 1 mil gya.
print(list3.index(66))#Output:3
print(list3.count(1))# 1 kinne vaar au. Answer: do vaar.
# print(list3.reverse())#Output :None Why?,reverse function ne kujh return nahi kita islayi none ya.Correct approach to do same task:
list3.reverse()
print(list3)
m=list3# Isda mtlab eh hoya ki list3 da reference apa m nu de dita te jehda change list m ch hou oh list3 ch vi hou jehda ki apa real world projects ch nah chahunde hunde  islayo copy function use karange.
# m[0]=0
# print(m)
# print(list3)
m=list3.copy()
m[0]=0
print(list3) #No change in original list
list3.insert(1, 13)#means list de index number 1 te element=13 nu add kardo.
print(list3)
n=[1,2,3,4,5,6,7,8,9,10]
j= n + list3 # List concatenation
print(j)
list3.extend(n)#means list n de sare elements ,list 3 ch paado.
print(list3)



