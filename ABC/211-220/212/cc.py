n,m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#print(abs(a[0]-b[0]))
w = 10**9
for i in range(n):
    for j in range(m):
        x = abs(a[i]-b[j])
        w = min(w,x)
print(w)