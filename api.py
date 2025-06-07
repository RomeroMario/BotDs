from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from datetime import datetime
from db import guardarConfesión

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
    try:
        with open("/etc/secrets/confesiones.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()
            if lineas:
                return lineas
            else:
                return []
    except FileNotFoundError:
        return []

@app.post("/lectura")
async def lectura(id: int):
    try:
        with open("/etc/secrets/confesiones.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()
            if lineas:
                for i, linea in enumerate(lineas):
                    if int(linea.split("&")[0]) == id:
                        lineas[i] = linea.replace("False", "True")
                        break
                with open("confesiones.txt", "w", encoding="utf-8") as f:
                    f.writelines(lineas)
                return {"message": "Confesión marcada como leída"}
            else:
                return {"message": "No se encontraron confesiones"}
    except FileNotFoundError:
        return {"message": "No se encontraron confesiones"}



async def save_confess( confesion: str):
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    guardarConfesión(confesion, fecha_actual, "False")
    