n,x = map(int,input().split())
a = list(map(int,input().split()))
total = sum(a)-n//2
if total <= x:
    print("Yes")
else:
    print("No")