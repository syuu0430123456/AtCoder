a, b = map(int,input().split())
f = 2*a+100
if b >= f:
    print(0)
else:
    print(f-b)