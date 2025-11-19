matrix1 = [list(map(int,input().split())) for i in range(3)]
input()
matrix2 = [list(map(int,input().split())) for i in range(3)]

for i in range(3) : 
    for j in range(3) : 
        print(matrix1[i][j] * matrix2[i][j],end =' ')
    print()