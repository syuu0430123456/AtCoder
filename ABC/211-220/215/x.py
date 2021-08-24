import sys
import itertools

def unique(iterable):
    seen = set()
    for x in iterable:
        if x in seen:
            continue
        seen.add(x)
        yield x

s,k = sys.stdin.readline().split()
k = int(k)
s = sorted(s)
l = []
for i in unique(itertools.permutations(s)):
    l.append[i]
print(l)