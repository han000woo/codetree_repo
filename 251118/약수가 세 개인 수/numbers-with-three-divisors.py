import math 

start, end = map(int, input().split())

def is_prime(n) :
    if(n<2) :
        return False
    for i in range(2,int(math.sqrt(n))+1) :
        if(n%i == 0) :
            return False 
    return True 
        
# Please write your code here.
count = 0
num = start 
for i in range(start, end+1) :
    root= int(math.sqrt(i))
    if (root * root == i and is_prime(root)) :
        count +=1
print(count)