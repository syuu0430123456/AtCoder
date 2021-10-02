s = input()
t = input()
ans = 'No'

if s == t:
    ans = 'Yes'

for i in range(len(s)-1):
    x = list(t)
    x[i],x[i+1] = x[i+1],x[i]
    y = ''.join(x)
    if s == y:
        ans = 'Yes'
        break

print(ans)