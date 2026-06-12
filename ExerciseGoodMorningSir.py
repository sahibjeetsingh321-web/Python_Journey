#Create a python program capable of greetibg you with Good Morning, Afternoon, Evening, Night. Your program should use time module to get the current hour. 
import time
timestamp = time.strftime("%H:%M:%S")
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime("%S") # single te double quotes da koi chakkar nahi.
print(timestamp)
# %H,%M,%S hamesha hi eh upper case ch paune ne.
current_hour =int(time.strftime("%H"))
if(current_hour>=0 and current_hour<5):
    print("Amritvela ho gya bhai.Rabb da naam lailo")
elif(current_hour>=5 and current_hour<12):
    print("Good Morning")
elif(current_hour>=12 and current_hour< 17):
    print("Good Afternoon")
elif(current_hour>=17 and current_hour<20):#20 means 8 vaje
    print("Good evening")
else:
    print("Good Night")

#Clock system sirf 0 to 23:59:59 tak count karda islayi jekar raat layi logic likhna vi hove ta 
#elif current_hour>=20 likh deage is naal interpreter 20 to lai ke 23:59:59 layi Good Night print karu. 













#https://docs.python.org/3/library/time.html#time.strftime