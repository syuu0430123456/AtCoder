n = int(input())
division = []
for i in range(1,int(n**0.5)+1):
    if n%i == 0:
        division.append(i)
        if i!=n//i:
            division.append(n//i)

division.sort()
for i in division:
    print(i)