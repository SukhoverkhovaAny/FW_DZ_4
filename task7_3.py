# Задание №7
# � Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# � Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# � Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# � При решении задачи нужно использовать асинхронность.
# � В каждом решении нужно вывести время выполнения
# вычислений.
import random
import time
import asyncio


arr = [random.randint(1, 100) for i in range(1000001)]


async def sum_arr(array):
    summa = 0
    for i in range(len(array)):
        summa += i
        print(time.time())
    return summa


if __name__ == '__main__':

    tasks = []

    for i in arr:
        task = asyncio.ensure_future(sum_arr(i))
        tasks.append(task)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))