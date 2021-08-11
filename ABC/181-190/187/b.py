n = int(input())
for i in range(n):
    x,y = list(map(int,input().split()))

ans = 0
for i in range(n):
    for j in range(n):
        if i != j:
            t = (y[i]-y[j])/(x[i]-x[j])
            if t > -1 and t < 1:
                ans += 1
print(ans)