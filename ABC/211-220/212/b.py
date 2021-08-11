x = input()
l = [int(x) for x in list(str(x))]
#4桁同じ
if len(set(l))==1:
    print("Weak")
    exit()
#連番
t = []
for i in range(l[0],l[0]+4):
    t.append(i)
for j in range(len(t)):
    if t[j]>=10:
        t[j]= t[j]-10
if l == t:
    print("Weak")
else:
    print("Strong")