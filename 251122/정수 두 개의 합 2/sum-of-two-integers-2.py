n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort() 

left = 0
count = 0
for right in range(1, len(arr)) :

    while(arr[left] + arr[right] <= k) :
        count += 1
        left +=1 
print(count)

