answer = 0
for i in range(4) : 
    arr = list(map(int,input().split()))
    answer += sum(arr[:i+1])

print(answer)