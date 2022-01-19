s = input()
ans = 3
if s[0]==s[1] and s[1]==s[2]:
    ans = 1
elif s[0]!=s[1] and s[1]!=s[2] and s[0]!=s[2]:
    ans = 6
print(ans)