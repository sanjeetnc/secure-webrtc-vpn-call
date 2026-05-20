import asyncio
import json
import websockets


async def test():

    uri = "ws://127.0.0.1:8000/ws/call/testroom/"

    async with websockets.connect(uri) as websocket:

        print("Connected to signaling server")

        await websocket.send(json.dumps({
            "message": "hello from mac",
            "sender": "mac"
        }))

        print("Message sent")

        response = await websocket.recv()

        print("Received:")
        print(response)


asyncio.run(test())