import asyncio
import time

async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование.')
    for i in range(1, 6):
        print(f'Силач {name} поднял {i} шар')
        await asyncio.sleep(1/power)
    print(f'Силач {name} закончил соревнование')

async def start_tournament():
    tasks = [
        asyncio.create_task(start_strongman('Dima', 5)),
        asyncio.create_task(start_strongman('Andrei', 3)),
        asyncio.create_task(start_strongman('Zhenya', 7 ))
    ]
    await asyncio.gather(*tasks)

asyncio.run(start_tournament())
