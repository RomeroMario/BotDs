import asyncio
import uvicorn
from api import app
from bot import bot
from variables import TOKEN

async def run_fastapi():
    config = uvicorn.Config(app=app, host="127.0.0.1", port=8000, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    asyncio.create_task(run_fastapi())  # Inicia FastAPI
    await bot.start(TOKEN)              # Inicia el bot

if __name__ == "__main__":
    asyncio.run(main())
