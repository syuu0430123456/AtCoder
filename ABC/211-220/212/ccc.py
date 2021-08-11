import sys

def findsmalldifference(A,B,m,n):
    A.sort
    B.sort

    a = 0
    b = 0

    result = 10**9

    while(a < n and b < m):
        ans = abs(A[a] - B[b])
        
        result = min(ans,result)

        if A[a]<B[b]:
            a += 1
        else:
            b += 1
    return result
n,m = map(int,input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(findsmalldifference(A,B,n,m))