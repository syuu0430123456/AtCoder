n,k = map(int,input().split())
p = list(map(int,input().split()))

p.sort()
tot = 0
for i in range(k):
    tot += p[i]
print(tot)