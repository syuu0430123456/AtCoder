n,a,x,y = map(int,input().split())
tot =0
if n<=a:
    tot = n*x
else:
    tot = a*x+(n-a)*y
print(tot)