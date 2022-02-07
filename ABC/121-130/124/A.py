A,B = map(int, input().split())

a = A + A-1
b = B + B-1
c = A + B

print(max(a,b,c))