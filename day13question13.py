#  write the programmer to calculate componed interest
rate =int(input("Enter a  rate value->"))
principle= int(input("Enter a  principle interst->"))
time =int(input("Enter a  time->"))
Amount = principle*(1+rate/100)**time
print(Amount)
component = Amount-principle
print(component)