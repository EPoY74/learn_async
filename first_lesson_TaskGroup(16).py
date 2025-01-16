import asyncio
import time

async def print1(sec:int):
    await asyncio.sleep(sec)
    print(sec)


async def main():
    async with asyncio.TaskGroup() as tg:
        for i in range(1,16):
            tg.create_task(print1(i))

start = time.time()
asyncio.run(main())
print(f"Время на работу: {time.time() - start}")

