import api
import asyncio

async def send_data(to: str):
    print(f'sending data to {to}')
    await asyncio.sleep(2)
    print('sending Data to {to}')

async def main():
    data = await api.fetch_data()
    print('data:', data)
    
    await send_data('Mario')

if __name__ == '__main__':
    asyncio.run(main())
