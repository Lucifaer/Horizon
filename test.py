from core.dispatcher import Dispatcher
import asyncio

if __name__ == '__main__':
    test = Dispatcher('secwiki')
    asyncio.run(test.start())
