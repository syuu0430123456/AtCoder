s = input()
cnt = 0
for i in range(3):
    if s[i]=="o":
        cnt +=1
total = 700 + cnt*100
print(total)