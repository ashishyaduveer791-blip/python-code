num =int(input("Enter a number"))
sum = 0 
temp = num
while temp > 0:
    digit = temp%10
    cube = digit**3
    sum = sum +cube
    temp //= 10
    if sum == num:
        print('it is an armstorgn number:')
    else:
        print("It is not armstrong number:")