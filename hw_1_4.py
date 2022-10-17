str_list = ['разработка', 'администрирование', 'protocol', 'standard']

for item in str_list:
    print('Исходная строка: ', item)
    byte_str = item.encode('utf-8')
    print('В виде байтов: ', byte_str, type(byte_str))
    back_to_str = byte_str.decode('utf-8')
    print('После обратного преобразования к строковому типу: ', back_to_str, type(back_to_str))
    print('-' * 60)
