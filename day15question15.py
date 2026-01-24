#  Find ing factorial
# By using Recursion
num = int(input("Enter a  number-:"))
fact = 1
if num < 0:
    print("factorial of 0 does not exit")
    if num == 0:
        print("factorial of 0 is ",1)
        if num > 0:
            fact = fact * i
            print("the factorial of the given number is", fact)



# n =int(input("Enter a number->"))
fact = 1
for i in range(1,n+1):
    fact *= i
    print("Factorial:",fact)

#   One more another question


# Max  =6
# fact =[1]*(Max+1)
# for i in range(1, Max+1):
#     fact[1] = fact[i-1] * i
#     print(fact)
#     print(fact[5])


#  Using Built in Fuction(math.factorial)
import math
print("Factorial:" , math.factorial(5))
