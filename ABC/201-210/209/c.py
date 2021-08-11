N = int(input())
C = map(int,input().split())
a = 10**N - 2*(9**N) + 8**N

ans = a%(10**9+7)

print(ans)