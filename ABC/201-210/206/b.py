n = int(input())
ans = 0
for i in range(n):
    ans += i+1
    if ans >= n:
        print(i+1)
        exit()