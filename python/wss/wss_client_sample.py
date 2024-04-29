import websockets
import asyncio

async def test():
    async with websockets.connect('wss://demo.piesocket.com/v3/channel_1?api_key=YOUR_API_KEY') as websocket:

