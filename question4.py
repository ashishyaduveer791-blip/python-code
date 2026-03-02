# . Create a dictionary of n persons where key is name and value is city.  
# a) Display all names 
# b) Display all city names 
# c) Display student name and city of all students. 
# d) Count number of students in each city.

# .dictionary (get)
# d ={
#     'course':'python',
#     'fees':8000,
#     'duration':'2 Months'

# }
# c=d.get('course')
# print(c)
# # keys
# for a in d.keys():
#     print(a)
#     # values
#     for x in d.values():
#         print(x )
#         # iteam
#         for v ,b in d .items():
#             print(v,b)
# del d['fees']
# print(d)
# d.pop('duration')
# print(d)

# d=dict(name='ashish',city='koderma')
# print(d)
# d=update({'fees':10000})
# print(d)
#  when some one want to add new add add in the dicrotinary how i can do this
# d['desc']="This is pyhton"
# print(d)

d={
    'Ashish':'Jharkhand',
    'rupes':'Jharkhand',
    'Isha':'Rajsthan',
    'swastik':'Haryana',
    'sumit':'Uttarakhand',

}
for a in d.keys():
    
  
    print(a)
    for b in d.values():
        print(b)
        for n,m in d.items():
            print(n,m)
#            state_count = {}
#            for name in students:
#              state = students[name]
#               if state in state_count:
#                 state_count[state] += 1
#                  else:
#                      state_count[state] = 1
# print("Number of students in each state:")
# for state in state_count:
#      print(state, ":", state_count[state])




   
    
   
        
   
       

   
   
      
    