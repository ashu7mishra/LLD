import asyncio
import time

async def hello():
    await asyncio.sleep(1)
    print("hello")

async def func1():
    print("fun1")

# asyncio.run(hello())
# func1()

async def main():
    await asyncio.gather(hello(),func1())

asyncio.run(main())