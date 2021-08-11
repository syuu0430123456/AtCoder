s = input()
t = input()
S = sorted(s)
T = sorted(t,reverse=True)
S = "".join(S)
T = "".join(T)
if S < T:
    print("Yes")
else:
    print("No")