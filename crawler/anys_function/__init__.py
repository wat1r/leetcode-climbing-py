import asyncio
import threading

def sync_callback():
    # 同步操作
    threading.Event().wait(10)
    return "回调结果"

async def async_wrapper(func, *args):
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, func, *args)
    return result

async def main():
    result = await async_wrapper(sync_callback)
    print("这是一个结果")
    print(result)

# 运行事件循环
asyncio.run(main())