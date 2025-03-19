import os
import asyncio
import websockets

async def handler(websocket, path):
    async for message in websocket:
        print("Mesaj primit:", message)
        response = f"Salut! Ai trimis: {message}"
        await websocket.send(response)

async def main():
    port = int(os.getenv('PORT', 5000))  # folosește portul alocat de Render
    async with websockets.serve(handler, "0.0.0.0", port):
        print(f"Serverul pornește pe portul {port}")
        await asyncio.Future()  # serverul rulează la nesfârșit

if __name__ == "__main__":
    asyncio.run(main())
