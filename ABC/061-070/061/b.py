n, m = map(int,input().split())
l = [0 for i in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    l[a-1] += 1
    l[b-1] += 1
for i in l:
    print(i)