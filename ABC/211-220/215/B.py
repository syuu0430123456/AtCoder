n = int(input())

for i in range(100):
    if 2 ** i <= n:
        ans = i
print(ans)