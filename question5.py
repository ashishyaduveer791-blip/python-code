# Write the funtion  using lamda to print volume of cone
# import math
# square=lambda x:x *x
# print(square(5))
import math

Volume_of_cone=lambda r,h :(1/3)*math.pi*r**2*h
r = float(input("Enter ya number"))
h = float(input("enter a  number"))

print("Volume of cone=",Volume_of_cone(r,h))