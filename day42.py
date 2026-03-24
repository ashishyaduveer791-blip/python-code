# merge two dicnaary
# bar operator
# solution 1
dict1={ "ashis":90,"Isha":95}
dict2={"Isha":96,"shivan":98}
print(dict1|dict2)

# solution 2 **
dict1={ "ashis":90,"Isha":95}
dict2={"Isha":96,"shivan":98}
print({**dict1,**dict2})


# solution3  using copy and upadte method
dict1={ "ashis":90,"Isha":95}
dict2={"Isha":96,"shivan":98}
dict3= dict2.copy()
dict3.update(dict1)
print(dict3)