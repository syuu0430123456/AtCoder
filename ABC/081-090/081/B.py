n = int(input())
a = list(map(int,input().split()))

k = 0#これが0の間は計算を繰り返す
ans = 0

while k==0:
    for i in range(n):
        if a[i]%2 == 1:
            k=1
            break
        else:
            a[i]=a[i]//2
        if i == (n-1):
            ans +=1
print(ans)