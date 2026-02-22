#  print the  martix
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter elements of Matrix 1:")
matrix1 = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix1.append(row)

print("Enter elements of Matrix 2:")
matrix2 = []
for i in range(rows):
    row = list(map(int, input().split()))
    matrix2.append(row) # 

# Print matrices
print("\nMatrix 1:")
for r in matrix1:
    print(r)

print("\nMatrix 2:")
for r in matrix2:
    print(r)







            #  Another method
A  = [[1,5,9,],
      [7,8,2],
      [8,3,6]]
B = [[6,7,9],
     [4,2,6],
     [2,8,9]]
result=[[0,0,0,],
        [0,0,0,],
        [0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j]+B[i][j]
        for r in result:
            print(r)


