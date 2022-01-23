N, M = [int(_) for _ in input().split()]
S = input().split()
T = set(input().split())
ans = ['Yes' if s in T else 'No' for s in S]
print('\n'.join(ans))