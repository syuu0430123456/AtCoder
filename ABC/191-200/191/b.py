n,x=map(int,input().split())
a = list(map(int,input().split()))
for i in range(n):
    if x in a:
        a.remove(x)
print(a)
