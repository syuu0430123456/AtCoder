import sys
from itertools import permutations
s,k = sys.stdin.readline().split()
k = int(k)
s = sorted(s)
ans = []
ans_list = set(permutations(s))
for i in ans_list:
    print(i)

