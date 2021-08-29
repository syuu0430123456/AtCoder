n = int(input())

cnt = 0
for i in range(n):
    if i%3==0 or i%5==0 or i%15==0:
        cnt += 0
    else:
        cnt += i

print(cnt)