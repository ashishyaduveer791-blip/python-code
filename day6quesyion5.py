#  covert into  one unot o another unit
# To km to mile
# km = float(input(" Enter your values in kms: "))
# miles = (0.601271)*km
# print(km,"km in miles will be" , miles, "miles ")


# Another metthod( using fuction)
# def km_to_miles(km):
#     return km*0.621371
# km = float(input("Enter kilometer:"))
# print(km_to_miles(km))

# #  using lmada input 
# km = float(input("Enter kilometer:"))
# convert = lambda x:x*0.6213171
# print("Miles:" , convert(km))


# #  One More method
# Rate = 0.621371
# km = float(input("Enter   kilometer:"))
# print("Miles:", km * Rate)
      


    #   using class+input
# class convert:
#     def km_to_miles(self,km):
#         return km*0.621371
#     km = float(input("Enter kilometer:"))
#     obj = convert()
#     print("Mile:" , obj.km_to_miles(km))


#  using loop 
# km =  float(input("Enter kilomter:"))
# while True:
#     print("Miles:" , km *0.62137)
#     break


# using recursion
def convert():
    km =  float(input("Enter kilometer:"))
    print("Miles:" , km* 0.6213171)
    convert()

    
 