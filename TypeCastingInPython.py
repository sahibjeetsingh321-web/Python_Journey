a = "1"
# a = 1
b = "2"
# b = 2
print(int(a) + int(b))  # Explicit type casting

# Imlicit type casting
c = 1.9
d = 8
print(
    c + d
)  # answer will converted to float automatically because d will converted into float during operation
print(type(c + d))#float
print(type(d))  # It remains as integer but during operaion it is treated as float
