carbon = int(input('Введите количество атомов углерода для рассчёта формулы алкана(до 10 включительно'))
hydrogen = 2 * carbon + 2
formula = f'C{carbon}H{hydrogen}'
alkans = {
    'C1H4' : 'метан',
    'C2H6' : 'этан',
    'C3H8' : 'пропан',
    'C4H10' : 'бутан',
    'C5H12' : 'пентан',
    'C6H14' : 'гексан',
    'C7H16' : 'гептан',
    'C8H18' : 'октан',
    'C9H20' : 'нонан',
    'C10H22' : 'декан'
}
for a in alkans:
    if a == formula:
        x = alkans.get(a)
        print(f'{formula} - это {x}')
