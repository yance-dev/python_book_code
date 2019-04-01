import asyncio


def call_back(n, loop):
    print(f"callback {n} 运行时间点{loop.time()}")


async def main(loop):
    now = loop.time()
    print("当前的内部时间", now)
    print("循环时间", now)
    print("注册callback")
    loop.call_at(now + 0.1, call_back, 1, loop)
    loop.call_at(now + 0.2, call_back, 2, loop)
    loop.call_soon(call_back, 3, loop)
    await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        print("进入事件循环")
        loop.run_until_complete(main(loop))
    finally:
        print("关闭循环")
        loop.close()

"""
进入事件循环
当前的内部时间 39993.024
循环时间 39993.024
注册callback
callback 3 运行时间点39993.024
callback 1 运行时间点39993.133
callback 2 运行时间点39993.227
关闭循环
"""