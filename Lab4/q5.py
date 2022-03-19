amt = int(input('Enter the amount of money: '))
jeans = amt // 750
additional = ((jeans + 1) * 750) - amt
print('Number of jeans can be bought:', jeans)
print('Amount needed for additional jean: ', additional)
