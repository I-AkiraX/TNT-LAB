n = int(input('Enter a number: '))
c = 0

for i in range(2, n):
    if n%i == 0:
        c += 1
        break
if c != 0:
    print('Number is not prime')
else:
    print('Number is prime')
