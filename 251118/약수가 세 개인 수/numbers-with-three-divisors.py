import math 

start, end = map(int, input().split())

def is_prime(n) :
    for i in range(2,int(math.sqrt(n))+1) :
        if(n%i == 0) :
            return False 
    return True 
        
# Please write your code here.
count = 0
num = start 
for i in range(int(math.sqrt(start)), int(math.sqrt(end))) :
    if(is_prime(i)) :
        count +=1 
print(count)