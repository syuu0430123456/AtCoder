n=int(input())
a=[2**i for i in range(7)]
for i in range(7):
    if a[i]<=n:
        ans=a[i]
print(ans)