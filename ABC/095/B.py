N,X=map(int,input().split())
m=[int(input()) for i in range(N)]

for i in range(N):
    X -= m[i]
X = X//min(m)
print(X+N)