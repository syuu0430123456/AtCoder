a,b,c,x,y = map(int,input().split())

tot = 0
if a+b <= 2*c:
    tot = a*x + b*y
else:
    if x>=y & y%2==0:
        tot = y*2*c + a*(x-y)
    elif x>=y & y%2!=0:
        tot = y*2*c + a*(x-y) + y
    elif x<y & x%2==0:
        tot = x*2*c + b*(y-x)
    else:
        tot = x*2*c + b*(y-x) + x
print(tot)
