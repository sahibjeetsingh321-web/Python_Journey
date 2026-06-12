fruit = "Mango"
mangoLen = len(fruit)
print(mangoLen)
print(fruit[0:4])  # including 0 but not 4
print(fruit[1:4])  # including first index but not fourth
print(fruit[:5])  # by default starts from zero and goes to fift index
print(fruit[0:-3])  # minus 3 represents len(fruit)-3 means 5 - 3 = 2
print(fruit[-1 : len(fruit) - 3])
print(fruit[-3:-1])

# Quick Quiz
nm = "Harry"
print(nm[-4:-2])  # Explanation: len(fruit)=5
# [5-4:5-2]=[1:3] which means that interpreter will start print from first index and will go to the 3-1 index and the output will be 'ar'.
print(nm)
# Output???
