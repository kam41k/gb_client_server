str_list = ['attribute', 'класс', 'функция', 'type']

for item in str_list:
    if not item.isascii():
        print(f'"{item}" невозможно записать в байтовом типе')
