n = int(input())
status = False 
for i in range(n) :
    row = [] 
    for j in range(n):
        row.append(j+1)
    if(status) :
        row.reverse()
    status = not status
    for r in row :
        print(r,end='')
    print()