import asyncio
import websockets

async def handle_connection(websocket, path):
    async for message in websocket:
        print("Mesaj primit:", message)
        response = f"Salut! Ai trimis: {message}"
        await websocket.send(response)

async def main():
    # Serverul ascultă pe adresa și portul specificate
    async with websockets.serve(handle_connection, "0.0.0.0", 5000):
        await asyncio.Future()  # rulează la nesfârșit

if __name__ == '__main__':
    asyncio.run(main())
