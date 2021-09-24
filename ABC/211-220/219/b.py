s1 = input()
s2 = input()
s3 = input()
t = (input())
ans = []
for i in range(len(t)):
    if t[i]=="1":
        ans.append(s1)
    elif t[i]=="2":
        ans.append(s2)
    elif t[i]=="3":
        ans.append(s3)
print(''.join(ans))