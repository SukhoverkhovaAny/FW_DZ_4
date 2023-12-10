# Задание №5
# � Создать программу, которая будет производить подсчет
# количества слов в каждом файле в указанной директории и
# выводить результаты в консоль.
# � Используйте процессы.

import os
import multiprocessing

PATH = 'D:\training\6. Frameworks\DZ\DZ_4'


def parser_text(file_name: str):
    with open(file_name, 'r', encoding='UTF-8') as file:
        content = file.read()
        count = len(content.split())
        print(f'{file_name} count = {count}')


processes = []


def process_count(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            p = multiprocessing.Process(target=parser_text, args=(file_path))
            processes.append(p)
            p.start()


if __name__ == '__main__':
    process_count(PATH)

    for process in processes:
        process.start()

    for process in processes:
        process.join()