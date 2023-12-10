# Задание №4
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте потоки.
import os
import threading

PATH = 'D:\training\6. Frameworks\DZ\DZ_4'


def parser_text(file_name: str):
    with open(file_name, 'r', encoding='UTF-8') as file:
        content = file.read()
        count = len(content.split())
        print(f'{file_name} count = {count}')


threads = []


def threads_count(directory):
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                t = threading.Thread(target=parser_text, args=(file_path))
                threads.append(t)
                t.start()

if __name__ == '__main__':
    threads_count(PATH)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()