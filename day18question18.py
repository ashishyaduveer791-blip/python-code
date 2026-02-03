n = int(input("Enter number:"))
# x = int(input(" Sum of natural number:"))
sum= (n*n+n)//2
print("Sum of natural number is:",sum) 

#  logic  buliding
n = int(input("Enter number:"))
total = 0
for i  in range(1 ,n+1):
    total +=i
    print("Sum = ",total)

    #  interrviews level question
    n = int(input("Enter a number:"))
    i =1
    total = 0
    while i<=n:
        total +=i
        i+=1
        print("sum=" ,total)

        # Advanced level
n = int(input("Enter a number:"))
print("sum = ",sum(range(1,n+1)))
    
 
