n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
visited_dict = {} 
for i in arr :
    if i in visited_dict :
        visited_dict[i] +=1 
    else : 
        visited_dict[i] = 1

count = 0
for key in visited_dict.keys() :
    if(visited_dict[key] == 0) :
        continue
    alter_key = k - key 
    if(visited_dict[alter_key] == 0) :
        continue 
    visited_dict[key] -= 1
    visited_dict[alter_key] -=1
    count +=1

        

print(count)