arr = list(map(int,input().split()))
dice_dict= {} 
for i in range(1,7) :
    dice_dict[i] = 0 
for i in arr : 
    dice_dict[i] += 1 
for k,v in dice_dict.items() :
    print(f'{k} - {v}')