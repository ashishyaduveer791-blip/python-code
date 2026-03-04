# Create a contact book where users can store, search, update, and delete contacts. Use 
# dictionary for storing contacts. 
# contacts = {}

# while True:
#     print("\n------ CONTACT BOOK ------")
#     print("1. Add Contact")
#     print("2. Search Contact")
#     print("3. Update Contact")
#     print("4. Delete Contact")
#     print("5. Show All Contacts")
#     print("6. Exit")

#     choice = input("Enter your choice: ")

    
#     if choice == '1':
#         name = input("Enter Name: ")
#         phone = input("Enter Phone Number: ")
#         contacts[name] = phone
#         print("Contact Added Successfully!")


#     elif choice == '2':
#         name = input("Enter Name to Search: ")
#         if name in contacts:
#             print("Phone Number:", contacts[name])
#         else:
#             print("Contact Not Found!")

 
#     elif choice == '3':
#         name = input("Enter Name to Update: ")
#         if name in contacts:
#             new_phone = input("Enter New Phone Number: ")
#             contacts[name] = new_phone
#             print("Contact Updated Successfully!")
#         else:
#             print("Contact Not Found!")

   
#     elif choice == '4':
#         name = input("Enter Name to Delete: ")
#         if name in contacts:
#             del contacts[name]
#             print("Contact Deleted Successfully!")
#         else:
#             print("Contact Not Found!")

  
#     elif choice == '5':
#         if contacts:
#             print("\nAll Contacts:")
#             for name in contacts:
#                 print(name, ":", contacts[name])
#         else:
#             print("No contacts available.")

  
#     elif choice == '6':
#         print("Exiting Contact Book...")
#         break

#     else:
#         print("Invalid Choice! Try Again.")




#  Create a contact book where users can store, search, update, and delete contacts. Use 
# dictionary for storing contacts.

# movies_name=input("Enter a movies name:")
# years=list(map(int,input("Enter years:").split()))
# director=input('Enter a director name:')
# cost=list(map(int,input("Enter cost:").split()))
# collection=list(map(int,input("Enter collection:").split()))

# movies={
#     'Movies_name':movies_name,
#     "Years":years,
#     "Director":director,
#     "Production cost":cost,
#     "Collection":collection,

# book=input("Enter a book name:")
Book={
    'book_name1':'good English',
    'book_name2':'As arrawall',
    'book_name3': 'RD sharma',
    'book_name4':'Bipan yadva',
}
# search
search=input("Enter book name:")
if search in Book.values():
   print("Book found")
else:
   print("Book not found")
   
   
# keys
for a in Book.keys():
   print(a)

# update
# d=update({'fees':10000})
# print(d)
Book.update({'book_name2':'Evs'})
print(Book)
# del d['fees']
# print(d)
del Book['book_name1']
print(Book)











