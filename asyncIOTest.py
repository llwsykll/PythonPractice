import asyncio

# 把一个generator标记为coroutine类型，
# 然后，我们就把这个coroutine扔到EventLoop中执行
@asyncio.coroutine
def hello():
    print("Hello world!")
    # 异步调用sleep
    r = yield from asyncio.sleep(1)
    print("Hello again!")

# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()