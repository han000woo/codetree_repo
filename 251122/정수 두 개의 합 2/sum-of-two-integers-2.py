n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort() 

left = 0
count = 0
right = 1
len_Arr = len(arr)
while(left < right) : 
    # print(left,right)
    while( arr[left] + arr[right] <= k) :
        # print("inner",left,right)
        count += 1
        if(right + 1 == len_Arr) :
            break
        right +=1

    left += 1
print(count)

