# m =int(input("Enter a number"))
# if(m%2 ==0):
#     print("IT WILL EVEN NUMBER->m")

    


# else:
#     print("IT WILL ODD NUMBER->m")

    #  Another method
    #  Using BItwise And (&) Operator
# n = int(input("Enter a number:"))
# if n & 1:
#         print("Odd")
# else:
#         print("Even")

# using lamdaa function

# is_even = lambda n: "Even" if n% 2==0 else"odd"
# print(is_even(8))


# usiing  short & smart
# n = int(input("Enter a number:"))
# result=["Even" , "Odd"]
# print(result[n%2])


# Usig Recusrsion
def check_even(n):
    if n ==0:
        return "Even"
    if n ==1:
        return"odd"
    return check_even(n-2)
m =int(input("Enter a number:"))

print(check_even(m))


        

