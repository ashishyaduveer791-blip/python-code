# Scan n values in range 0-3 and print the number of times each value has occurred.
n = input("Enter a number:")
# create empty list 
numbers =[]
for i in range(n):
    num=int(input("Enter value(0,9):"))
    numbers.appened(num)
    for i in range(0,10):
        print(i,"occured",numbers.count(i),"time")