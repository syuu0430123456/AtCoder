n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
k = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i]%a[j] == 0:
            ans = max(a[i]/a[j], ans)
print(ans)