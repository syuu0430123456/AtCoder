L, R = map(int, input().split())
s = input()
s = list(s)
s_rev = s[L-1:R]
s_rev.reverse()

new_s = s[:L-1] + s_rev +s[R:]

print(''.join(new_s))