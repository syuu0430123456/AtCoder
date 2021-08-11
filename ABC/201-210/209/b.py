n,x = map(int,input().split())
a = list(map(int,input().split()))
t = 0
U = sum(a)
for i in range(n):
    if i%2==1 and a[i]!=1:
        t +=1
U = U-t
if U <= x:
    print("Yes")
else:
    print("No")