# write the program to print series
#  1+1/2+1/3 ......1/n
num = 5
sum =0
for i in range(1,num+1):
    sum=sum+1/i
    print(f"1{i}")
    print("sum=",sum)
