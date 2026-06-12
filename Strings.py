name = "Sahib Singh"
friend = "Guru Maharaj"
anotherFriend = "Guru De Pyare"

talk = '''
He said,"Kyun Bhra Ki Haal Chaal Ne??
Hor Ghare Kive Ne Saare??"'''

print("Sat Sri Akaal," + name)  # concatenation using plus
print("Sat Sri Akaal," + name, "Ji")
print(talk)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])  # This index is for space  which is in between Sahib and Singh
print(name[6])
print(name[7])
print(name[8])
print(name[9])
print(name[10])
# print(name[11]) -> Throws an error
print('"Lets use a for loop"\n')
for character in name:
    print(character)  # uppar wala lamba chauda kamm for loop ne asaan karta:-> print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# print(name[5])  # This index is for space  which is in between Sahib and Singh
# print(name[6])
# print(name[7])
# print(name[8])
# print(name[9])
# print(name[10])
