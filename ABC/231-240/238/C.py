N = int(input())
ans = 0
for i in range(len(str(N))-1):
    if i==0:
        ans = (10-1)*(10//2)
        #ans += (10**i -1)*((10**i)//2)
    else:
        bnt = (9 * 10**i +1) * (9 * 10**i)//2
        ans += bnt

b = N - 10**(len(str(N))-1) +1
ans += b*(b+1)//2

print(ans%998244353)