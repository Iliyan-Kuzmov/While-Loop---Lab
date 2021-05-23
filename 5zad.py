suma = input()
total = 0.0
while suma != 'NoMoreMoney':
    amount = float(suma)

    if amount < 0:
        print('Invalid operation!')
    total += amount
    print(f'Increase: {amount:.2f}')
    suma = input()
print(f'Total: {total:.2f}')