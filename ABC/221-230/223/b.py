s = input()

smin = sorted(s)
smax = sorted(s, reverse=True)
print(''.join(smin))
print(''.join(smax))