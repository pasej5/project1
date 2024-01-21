#!/usr/bin/env python3
import asyncio

"""async def main():
    print("Well done for a great year")
    task = asyncio.create_task(foo())
    await asyncio.sleep(5)
    print("finished")

async def foo():
    print("It's been tought but you made it")
    await asyncio.sleep(2)


asyncio.run(main())"""


async def fetch_data():
    print('starting')
    await asyncio.sleep(2)
    print('done fetching')
    return {'data': 1}

async def print_number():
    for i in range(10):
        print(i)
        await asyncio.sleep(2)
        
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(print_number())
    
    value = await task1
    print(value)

asyncio.run(main())