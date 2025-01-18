import asyncio
import time


async def do_something(sec:int) -> None:
    """Смысл ввода этой функции - что бы показать, что при её вызове не надо
    её также добавлять в группу задач. 

    Args:
        sec (int): Число. Берется из запускающнго цикла
    """
    await asyncio.sleep(sec)
    print(f"result: {sec}")


async def print1(sec:int):
    await asyncio.sleep(sec)
    print(sec)
    await do_something(sec)


async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1,16):
            tg.create_task(print1(i))

start = time.time()
asyncio.run(main())
print(f"Время на работу: {time.time() - start}")

