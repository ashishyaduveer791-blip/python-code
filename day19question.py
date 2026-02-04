nterm=int(input("Enter number of term here:"))
result= list(map(lambda x : 2**x,range(nterm+1)))
print(result)
for i in range(nterm+1):
    print("The values of 2 raisedd to power",i,"is",result[i])