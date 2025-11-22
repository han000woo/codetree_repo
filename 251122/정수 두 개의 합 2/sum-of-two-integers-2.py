n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]

# Please write your code here.
arr.sort()
left = 0
right = n - 1
count = 0

while left < right:
    if arr[left] + arr[right] <= k:
        count += (right - left)
        left += 1
    else:
        right -= 1

print(count)