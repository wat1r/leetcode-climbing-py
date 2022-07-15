import asyncio
import websockets
import time


# weibo login rpc

async def check_permit(websocket):
    for send_text in ["123@qq.com,12345", "123@qq.com,1111"]:
        await websocket.send(send_text)
    return True


async def recv_msg(websocket):
    while True:
        recv_text = await websocket.recv()
        print(recv_text)


async def main_login(websocket, path):
    await check_permit(websocket)
    await recv_msg(websocket)


start_server = websockets.serve(main_login, "127.0.0.1", 9876)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
