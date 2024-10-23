carbon = int(input('Введите количество атомов углерода для рассчёта формулы алкана'))
hydrogen = 2 * carbon + 2
formula = f'C{carbon}H{hydrogen}'
print(formula)