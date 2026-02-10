# Convert binary to decimall
decimal = int(input('Enter a numberr here:'))
print("The conversion of decimal number", decimal,"is:")
print(bin(decimal),"in binary")
print(oct(decimal),"in octadecimal")
print(hex(decimal)," hexdecimal")

# Advance versionn

binary =input("Enter a number:")
if all(bit in'01'for bit in binary):
    decimal=int(decimal,2)
    print("Decimal:",decimal)
    print("octal:",oct(decimal))
else:

    print("Invild binary number:")