"""

ИСточник урока:  https://www.youtube.com/watch?v=_4QY1nGFRY8&t=2156s
"""

import asyncio

async def print1():
    """Выводим число 1
    """
    print(1)

async def print2():
    """Ожидаю и вывожу число 2
    """
    print("I am sleeping. I am num 2")
    await asyncio.sleep(10)
    print("I am num 2. I woke up!")

async def print3():
    """Выводим число 3
    """
    print(3)


async def main():
    """Функция для запуска всего кода
    """
    task1 = asyncio.create_task(print1())
    task2 = asyncio.create_task(print2())
    task3 = asyncio.create_task(print3())

    await task1
    await task2
    await task3


# Запускаю событийный цикл
asyncio.run(main())
