import platform
import subprocess
import chardet

urls = ['yandex.ru', 'youtube.com']
code = '-n' if platform.system().lower() == 'windows' else '-c'

for url in urls:
    args = ['ping', code, '4', url]
    ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in ping.stdout:
        result = chardet.detect(line)
        print(result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
'''
Не до конца понял как реализовать через функцию locale.getpreferredencoding().
Выдает кодировку "cp1251" а в сообщениях используются "ascii" и "IBM866"
'''
