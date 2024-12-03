import os.path
import os

with open('recepty.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count()):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[recepie_name] = ingredients


def get_shop_list_by_dishes(person_count: int, dishes: dict):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['product'] in result:
                    result[consist['product']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['product']] = {'measure': consist['measure'],
                                                  'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)


get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])


file_names = ['1.txt', '2.txt', '3.txt']
file_info = []

for file_name in file_names:
    with open(file_name, 'r', encoding='UTF-8') as file:
        lines = file.readlines()
        line_count = len(lines)
        file_info.append((file_name, line_count, lines))

file_info.sort(key=lambda x: x[1])

with open('result.txt', 'w', encoding='UTF-8') as f:
    for file_name, line_count, lines in file_info:
        counting = 0
        for line in lines:
            f.write(f'Cтрока номер {counting} файла номер {file_name} : {line.strip()}\n')
            counting += 1
