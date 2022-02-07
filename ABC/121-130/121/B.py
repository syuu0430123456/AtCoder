N,M,C = map(int,input().split())
B = list(map(int,input().split()))
cnt = 0
ans = 0
for _ in range(N):
    A = list(map(int,input().split()))
    
    for j in range(M):
        ans += A[j]*B[j]
    ans += C
    if ans > 0:
        cnt += 1

print(cnt)