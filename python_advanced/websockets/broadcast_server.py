#!/usr/bin/env python3
"""WebSocket broadcast server."""

import asyncio
import websockets

connected_clients = set()


async def connection_handler(websocket):
    """Handle client connections and broadcast messages."""
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            disconnected = set()

            for client in connected_clients.copy():
                try:
                    await client.send(f"B:{message}")
                except websockets.exceptions.ConnectionClosed:
                    disconnected.add(client)

            connected_clients.difference_update(disconnected)

    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the broadcast server."""
    async with websockets.serve(
        connection_handler, "127.0.0.1", 8765
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
