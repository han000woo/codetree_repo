n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
visited_dict = {} 
for i in arr :
    visited_dict[i] = False 

count = 0
for key in visited_dict.keys() :
    if(visited_dict[key]) :
        continue 
    alter_key = k - key 
    if(alter_key == key) : 
        continue
    if(alter_key in visited_dict.keys()) :
        visited_dict[alter_key] = True 
        count +=1 

print(count)