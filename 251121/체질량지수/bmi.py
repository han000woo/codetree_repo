h,w = map(int,input().split())
res = (10000 * w) // (h*h)

print(res)
if(res>=25) :
    print("Obesity")