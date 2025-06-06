import asyncio
import uvicorn
from uvicorn.config import LOGGING_CONFIG as DEFAULT_UVICORN_LOGGING
from api import app
from bot import bot
from variables import TOKEN,URL,PORT
import os

def custom_log_config():
    log_config = DEFAULT_UVICORN_LOGGING.copy()

    # Personalizar formateador por defecto (logs generales)
    log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelprefix)s %(message)s"
    log_config["formatters"]["default"]["datefmt"] = "%Y-%m-%d %H:%M:%S"

    # Personalizar logs de acceso (peticiones HTTP)
    log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelprefix)s %(client_addr)s - \"%(request_line)s\" %(status_code)s"
    log_config["formatters"]["access"]["datefmt"] = "%Y-%m-%d %H:%M:%S"

    return log_config

async def run_fastapi():
    config = uvicorn.Config(
        app=app, 
        host=URL, 
        port=int(os.environ.get("PORT", PORT)) if os.environ.get("PORT") or PORT else 4000, 
        log_level="info" , 
        log_config=custom_log_config() 
        )
    
    server = uvicorn.Server(config)
    await server.serve()

async def main():
    asyncio.create_task(run_fastapi())  # Inicia FastAPI
    await bot.start(TOKEN)              # Inicia el bot

if __name__ == "__main__":
    asyncio.run(main())
