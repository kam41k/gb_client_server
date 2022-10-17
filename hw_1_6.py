from chardet import detect

str_list = ['сетевое программирование', 'сокет', 'декоратор']
with open('file.txt', 'w') as file:
    for line in str_list:
        file.write(f'{line}\n')

# узнаем кодировку файла
with open('file.txt', 'rb') as f:
    file_bytes = f.read()
encoding = detect(file_bytes)['encoding']

# открываем файл в правильной кодировке
with open('file.txt', 'r', encoding=encoding) as file:
    print(file.read())
