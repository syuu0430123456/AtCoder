s = list(map(int,input().split()))
s.sort()

if s[1]==s[0]:
    print(s[2])
elif s[1]==s[2]:
    print(s[0])
else:
    print(0)