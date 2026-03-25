# accesing indwx of the list uaing  for loop in python
l = [35,60,85,79]
for index,value in enumerate(l,start=1):
    print(index,"-",value)

    # using second method
    l =[41,52,85,74,56]
    for index in range(len(l)):
        value = l[index]
        print(index,value)
