count = 0 
for i in range(4) : 
    arr = list(map(int,input().split()))
    for i in arr :
        if i%5 == 0:
            count += 1
print(count)
