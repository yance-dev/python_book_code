import asyncio


def callback(n):
    print(f"callback {n} invoked")


async def main(loop):
    print("注册callbacks")
    loop.call_later(0.2, callback, 1)
    loop.call_later(0.1, callback, 2)
    loop.call_soon(callback, 3)
    await asyncio.sleep(0.4)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main(loop))
    finally:
        loop.close()

"""
注册callbacks
callback 3 invoked
callback 2 invoked
callback 1 invoked
"""