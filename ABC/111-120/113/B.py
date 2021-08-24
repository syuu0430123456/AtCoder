n=int(input())
t,a = map(int,input().split())
h = list(map(int,input().split()))
ans=[]
for i in range(n):
    T = t-h[i]*0.006
    ans.append(abs(T-a))
Ans = ans.index(min(ans))+1
print(Ans)