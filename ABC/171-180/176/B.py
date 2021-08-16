n = input()
num_list = [int(i) for i in list(n)]
cnt = 0
for i in num_list:
    cnt += i
if cnt % 9 == 0:
    print("Yes")
else:
    print("No")