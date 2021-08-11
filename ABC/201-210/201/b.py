from operator import itemgetter
n = int(input())
list = []
for i in range(n):
    s,t = input().split()
    list.append([s, int(t)])

list.sort(key=itemgetter(1), reverse=True)
print(list[1][0])