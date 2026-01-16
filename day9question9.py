m=int(input("Enter a  year:"))
if(m%4==0):
    print("THIS YEAR IS LEEP")
else:
    print("THIS IS NOT LEEP:")

# Using  recurssion

# def is_leap(year):
#     if year % 400 ==0:
#         return True
#     if year % 100 ==0:
#         return False
#     if year % 4 ==0:
#         return True
#     return False
# year = int(input("Enter  Year:"))
# if is_leap(year):
#     print("Leap Year")
# else:
#     print("NOt a leap Year")



#  DEcorator -style Recusive Evalution
def leap(year):
    checks = [(400, True),(100,False),(4,True)]
    def check(i):
        if i == len(checks):
            return False
        d,val = checks[i]
        if year %d == 0:
            return val
        return check(i+1)
    return check(0)
year = int(input("Enter year:"))
print("Leap year" if leap (year) else"Not a leap Year")
    

    
