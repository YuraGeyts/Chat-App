### chat-backend/app/server.py

import socketio
from aiohttp import web
from . import events

# Create a Socket.IO server instance with CORS enabled
sio = socketio.AsyncServer(cors_allowed_origins='*')

# Create an aiohttp web app and attach the Socket.IO server to it
app = web.Application()
sio.attach(app)

# Register all socket event handlers
events.register(sio)