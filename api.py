from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from datetime import datetime
from db import guardarConfesión, modificarEstado,obtenerConfesiones

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get("/ping")
async def read_root():
    return {"message": "pong"}

@app.head("/ping")
async def read_root():
    return {"Te odio": "pong"}


@app.get("/confesiones")
async def get_confesiones():
    return obtenerConfesiones()

@app.post("/lectura")
async def lectura(id: str):
    modificarEstado(int(id))



async def save_confess( confesion: str):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    guardarConfesión(confesion, fecha_actual, "False")
    