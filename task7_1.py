# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать многопоточность.
# � В каждом решении нужно вывести время выполнения
# вычислений.
import random
import time
import threading

arr = [random.randint(1, 100) for i in range(1000001)]


def sum_arr(array):
    summa = 0
    for i in range(len(array)):
        summa += i
        print(time.time())
    return summa

if __name__ == '__main__':

    threads = []

    for i in arr:
        t = threading.Thread(target=sum_arr, args=(i))
        threads.append(t)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()   


