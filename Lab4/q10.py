n = int(input('Enter n (Factorial): '))

fact = 1
for i in range(2, n+1):
    fact *= i

print(fact)