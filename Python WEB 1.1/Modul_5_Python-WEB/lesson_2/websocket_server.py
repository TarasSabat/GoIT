import time
import asyncio
import websockets


async def hello(websocket):
    name = await websocket.recv()
    print(f"<<< {name}")

    # while True:               # Безперервна передача 'Tick'- 'Tuck'
    #     await asyncio.sleep(1)
    #
    #     current_time: int = int(time.time())
    #     try:
    #         if current_time % 2 == 0:
    #             await websocket.send('Tick')
    #         else:
    #             await websocket.send('Tuck')
    #     except websocket.exception.ConnectionCloseOK:
    #         pass

    await websocket.send(f"Checking database")

    await asyncio.sleep(3)

    await websocket.send(f"Some data for you, but one more check")

    await asyncio.sleep(1)

    await websocket.send(f"finish")


async def main():
    async with websockets.serve(hello, "localhost", 8765) as server:
        await server.server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nShutdown")
