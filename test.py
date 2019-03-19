from core.dispatcher import Dispatcher
import asyncio

if __name__ == '__main__':
    test = Dispatcher('xz')
    asyncio.run(test.start())
