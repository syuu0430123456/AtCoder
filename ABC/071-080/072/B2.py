s = input()
t =[]
for i in range(len(s)):
    if i%2==0:
        t.append(s[i])
print("".join(t))