n = int(input())
d = [int(input())for i in range(n)]
#print(d)
cnt=0
d = sorted(list(set(d)),reverse=True)
print(len(d))