K = int(input())

a = bin(K)
a = a.replace("1", "2")
print(a[2:])