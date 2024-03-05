#!/usr/bin/env python3
import asyncio
import time

async def brewCoffee():
    print("start brewCoffee")
    await asyncio.sleep(3)
    print('end brewCoffee')
    return "coffee Ready"

async def toastBagel():
    print("start toastBagel()")
    await asyncio.sleep(2)
    print("end toastBagel")
    return "bagel toasted"

async def main():
    start_time = time.time()
    
    # batch = asyncio.gather(brewCoffee(), toastBagel())
    # coffee_ready, bagel_ready = await batch
    coffee_task = asyncio.create_task(brewCoffee())
    bagel_task = asyncio.create_task(toastBagel())
    
    coffee_ready = await coffee_task
    bagel_ready = await bagel_task
    
    
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    print(f'Result of brewCoffee: {coffee_ready}')
    print(f'Result of toastBagel: {bagel_ready}')
    print(f'Total execution time: {elapsed_time:.2f} seconds')

if __name__ == "__main__":
    asyncio.run(main())
