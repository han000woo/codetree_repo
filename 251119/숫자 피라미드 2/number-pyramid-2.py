N = int(input())
count = 1
for i in range(1,N+1) : 
    for j in range(i) :
        print(count,end=' ')
        count+=1
    print()
