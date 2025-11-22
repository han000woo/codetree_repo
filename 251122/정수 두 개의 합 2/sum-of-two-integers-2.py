n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort() 

left = 0

right = len(arr)-1
count = 0 

while(left <right) :
    # print(left,right)
    sum_v = arr[left] + arr[right]
    if(sum_v < k) :
        left +=1 
        right +=1
        count +=1 
    elif(sum_v == k) :
        right -=1 
        count +=1 
    elif(sum_v > k ) :
        right -=1 

print(count)

