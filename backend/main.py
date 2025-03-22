### chat-backend/main.py

from app.server import app

# Entry point to run the aiohttp application
if __name__ == '__main__':
    import aiohttp.web
    aiohttp.web.run_app(app, port=5000)