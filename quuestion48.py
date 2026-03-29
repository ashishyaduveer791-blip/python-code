# sort dicr]tionary
marks={"ashih":23,"lalal": 85,"golu":54}
print(marks)
# sort the dicnary
sv = sorted(marks.items(),key =lambda x : x[1])
print(sv)
# solution 2(sort onlly the values)
v=sorted(marks.values())
print(v)