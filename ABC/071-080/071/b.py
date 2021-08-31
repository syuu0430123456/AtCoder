s = input()
word = "abcdefghijklmnopqrstuvwxyz"
ans = set(word) - set(s)
print("None" if len(ans) == 0 else min(ans))