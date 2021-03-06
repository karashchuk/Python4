#!/usr/bin/python3
__author__      = "Anatoly Karashchuk"
import os
import re
import sys
import urllib.request

""" Logpuzzle
На сервере лежит 9 изображений, являющихся частями одного изображения 
(фото дикой природы).

Дан лог файл веб-сервера, в котором среди прочих запросов содеражатся запросы
к этим изображениям. Нужно вытащить из файла url всех изображений и скачать их.
Затем создать файл index.html и собрать с его помощью все изображения в одну
картинку.

Вот что из себя представляет строка лога:
101.237.66.11 - - [05/Jun/2013:10:44:02 +0400] "GET /images/animals_07.jpg HTTP/1.1" 200 13632 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.93 Safari/537.36"

Замечание: для создания html файла можно использовать самую простую разметку:
<html>
<body>
<img src="img0.jpg"><img src="img1.jpg">...
</body>
</html>

Подсказка: скачать файлы можно двумя способами:

1. Воспользоваться функцией, сохраняющей url по заданному пути file_name:
urllib.request.urlretrieve(url, file_name)

2. Скачать url и сохранить в файле:
import urllib.request
import shutil
...
with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response, out_file)

"""


def read_urls(filename):
    try:
        f = open(filename,'r',encoding = "utf-8")
    except FileNotFoundError:
        print("Ошибка названия файла")
        sys.exit(1)
    text = f.read()
    reg = re.compile(r'GET /images/(.*?) HTTP/1.1', re.DOTALL)  
    im = []
    for x in reg.findall(text):
        if x not in im:
            im.append(x)
    """ 
    Возвращает список url изображений из данного лог файла,
    извлекая имя хоста из имени файла (apple-cat.ru_access.log). Вычищает
    дубликаты и возвращает список url, отсортированный по названию изображения.
    """
    return (im)
  

def download_images(img_urls, dest_dir):
    if os.path.exists(dest_dir):
        a=1
    else:
        os.makedirs(dest_dir)
    #print(os.listdir())
    myurls=[]
    for x in img_urls:
        urllib.request.urlretrieve('http://apple-cat.ru/images/' + x, dest_dir+'/img'+x[-6:])
        myurls.append(dest_dir + '/img'+x[-6:])
    #print (myurls)
    f=open('index.html','w+')
    f.writelines(['<html>','<body>'])
    for x in sorted(myurls):
        f.write('<img src="'+ x + '">')
    f.writelines(['</body>','</html>'])
    return
    """
    Получает уже отсортированный спискок url, скачивает каждое изображение
    в директорию dest_dir. Переименовывает изображения в img0.jpg, img1.jpg и тд.
    Создает файл index.html в заданной директории с тегами img, чтобы 
    отобразить картинку в сборе. Создает importдиректорию, если это необходимо.
    """
    # +++ваш код+++
  

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: [--todir dir] logfile')
        sys.exit(1)
        #args=['apple-cat.ru_access.log','img']

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print('\n'.join(img_urls))

if __name__ == '__main__':
    main()
