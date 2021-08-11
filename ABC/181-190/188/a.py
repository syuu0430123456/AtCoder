a=list(map(int,input().split()))
a.sort()
a[0] = a[0]+3
if a[0]>a[1]:
    print("Yes")
else:
    print("No")