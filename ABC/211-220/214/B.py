s,t = map(int,input().split())
cnt = 0
for a in range(s+1):
    for b in range(s+1-a):
        for c in range(s+1-a-b):
            if a*b*c <= t:
                cnt += 1
print(cnt)
