n,k = map(int,input().split())
a_i = list(map(int,input().split()))
a_i.sort()
cnt = 0
if k>=n:
    cnt += k//n
    k = k-k//n*n
    


