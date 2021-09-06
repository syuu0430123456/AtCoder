s = [input() for i in range(3)]

ans = ['ABC','ARC', 'AGC', 'AHC']

an = list(set(ans)-set(s))
print(''.join(an))