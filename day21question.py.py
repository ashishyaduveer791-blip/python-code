# 123454321
# 1234*4321
# 123 **321
# 12   ***21
# 1      ****1

n= 5
for i in range(n):
    for j in range(1,n-1+1):
        print(j,end="")
        print("*"*(2*i-1),end="")
        for j in range(n-i,0,-1):
            print(j,end="")
            print()