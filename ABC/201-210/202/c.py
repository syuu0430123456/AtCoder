s = input()
s = s[::-1]
if s[-2] == 6:
    s[-2] = 9
print(s[-2])