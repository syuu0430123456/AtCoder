for i in range(1,101):
    if i%5==0 and i%3==0:
        print("FizzBuzz", end=' ')
    elif i%5==0:
        print("Buzz", end=' ')
    elif i%3==0:
        print("Fizz", end=' ')
    else:
        print(i, end=' ')

""" FizzBuzz = []
for i in range(1,101):
    if i%5==0 and i%3==0:
        FizzBuzz.append("FizzBuzz")
    elif i%5==0:
        FizzBuzz.append("Buzz")
    elif i%3==0:
        FizzBuzz.append("Fizz")
    else:
        FizzBuzz.append(i)

print(FizzBuzz) """