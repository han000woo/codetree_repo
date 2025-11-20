arr = list(map(int,input().split()))
sum = 0
count = 0
for i in arr :
    if(i >= 250) :
        break 
    sum += i 
    count += 1
print(sum, sum/count)