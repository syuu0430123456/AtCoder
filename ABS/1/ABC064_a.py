r,g,b = map(int,input().split())

tot = 100*r + 10*g + b

if tot%4==0:
    print("YES")
else:
    print("NO")