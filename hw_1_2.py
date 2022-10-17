str_list = ['class', 'function', 'method']

for item in str_list:
    byte_str = eval(f"b'{item}'")
    print(byte_str, '  , type: ', type(byte_str), '  , length in bytes: ', len(byte_str))
    print('-' * 50)
