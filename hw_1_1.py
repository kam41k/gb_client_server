def print_type_value(items):
    for item in items:
        print(item, '  type:', type(item))
    print('-' * 40)


str_list = ['разработка', 'сокет', 'декоратор']

print_type_value(str_list)

uni_list = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
                '\u0441\u043e\u043a\u0435\u0442',
                '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']

print_type_value(uni_list)
