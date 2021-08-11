n,a,x,y = map(int,input().split())
tot =0
if n>=a:
    tot = a*x+(n-a)*y
else:
    tot = n*a

print(tot)