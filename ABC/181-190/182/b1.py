#ユークリッドの互除法
#a:  b:
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

t = 0
n = int(input())
a = list(map(int,input().split()))
for i in range(n):
    for j in range(i+1, n):
        ans = max(gcd(a[i],a[j]),t)
print(ans)