# . Store details of n movies in a dictionary by taking input from the user. Each movie must store 
# details like name,  year, director name, production cost, collection made (earning) & perform the 
# following :- 
# a) print all movie details 
# b) display name of movies released before 2015 
# c) print movies that made a profit. 
# d) print movies directed by a particular director. 
movies_name=input("Enter a movies name:")
years=list(map(int,input("Enter years:").split()))
director=input('Enter a director name:')
cost=list(map(int,input("Enter cost:").split()))
collection=list(map(int,input("Enter collection:").split()))

movies={
    'Movies_name':movies_name,
    "Years":years,
    "Director":director,
    "Production cost":cost,
    "Collection":collection,



}
print("\n movies Detail:")
for key,value in movies.items():

    print(key,":",value)
    if years <2015:
        print("movies released before 2015")
    else:
        print("it will floo:")
        #


        # c) print movies that made a profit. 
        movies_name=input("Enter a movies name:")
        cost=list(map(int,input("Enter cost:").split()))
        collection=list(map(int,input("Enter collection:").split()))

        movies={
                 'Movies_name':movies_name,
                  
                  "Production cost":cost,
                  "Collection":collection,
        }
        for x in movies.key():
            if cost<collection():
                print("it will profitable :")
            else:
                print("it show not prifotiablle:")







    
    
    
        
    

    
