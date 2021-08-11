n,m = map(int,input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#print(abs(a[0]-b[0]))
s1 = abs(max(a)-max(b))
s2 = abs(max(a)-min(b))
s3 = abs(min(a)-max(b))
s4 = abs(min(a)-min(b))

print(min(s1,s2,s3,s4))