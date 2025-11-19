n = int(input())
for i in range(n) :
    status = True
    for j in range(n) :
        if(status) : 
            print(i+1,end='')
        else :
            print(n - i,end='')
        status = not status 
    print()