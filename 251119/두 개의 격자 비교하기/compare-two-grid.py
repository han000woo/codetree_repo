N,M = map(int,input().split())
matrix1 = [ list(map(int,input().split())) for i in range(N)]
matrix2 = [ list(map(int,input().split()))  for i in range(N)]

for i in range(N) :
    for j in range(M) : 
        if(matrix1[i][j] == matrix2[i][j]) :
            print("0",end=' ')
        else :
            print("1",end=' ')
    print()