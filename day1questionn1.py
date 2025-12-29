a=int(input("Enter a First Number:-"))
b=int(input("Enter a Second Number:-"))
sum = a+b 
print("sum=",sum)

# Another way
def addnumber():
    a =float(input("Enter a First Number:"))
    b =float(input("EEnter a  second Number :"))
    return a +b
print(addnumber())

#   One more another way
a,b= map(float,input("Enter  two numberr separated by spaces:").split())
print("sum=",a+b)
             
    
         
         