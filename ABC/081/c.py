n = int(input())
A = list(map(int,input().split()))
cnt = 0
q = 1
while q == 1:
    for i in range(n):
        if A[i]%2==1:
            q = 0
            break
        else:
            A[i] = A[i]/2
        if i == n-1:
            cnt += 1
print(cnt)