"""

ИСточник урока:  https://www.youtube.com/watch?v=_4QY1nGFRY8&t=2156s
"""

import time

def print1():
    """Выводим число 1
    """
    print(1)

def print2():
    """Ожидаю и вывожу число 2
    """
    print("I am sleeping")
    time.sleep(10)
    print(2)

def print3():
    """Выводим число 1
    """
    print(3)


def main():
    """Функция для запуска всего кода
    """
    print1()
    print2()
    print3()


main()
