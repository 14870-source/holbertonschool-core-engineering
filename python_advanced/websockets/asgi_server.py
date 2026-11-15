#!/usr/bin/env python3
"""ASGI application with HTTP and WebSocket support."""

from starlette.applications import Starlette
from starlette.responses import FileResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    """Serve the HTML page."""
    return FileResponse("index.html")


async def javascript(request):
    """Serve the JavaScript file."""
    return FileResponse("chat.js")


async def stylesheet(request):
    """Serve the CSS file."""
    return FileResponse("style.css")


async def websocket_endpoint(websocket):
    """Echo messages received from WebSocket clients."""
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(
    routes=[
        Route("/", homepage),
        Route("/chat.js", javascript),
        Route("/style.css", stylesheet),
        WebSocketRoute("/ws", websocket_endpoint),
    ]
)
