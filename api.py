from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O especifica ["http://127.0.0.1:5500"]
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
        with open("confesiones.txt", "r", encoding="utf-8") as f:
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
        with open("etc/secrets/confesiones.txt", "r", encoding="utf-8") as f:
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
    
    try:
        with open("etc/secrets/confesiones.txt", "r", encoding="utf-8") as f:
            lineas = f.readlines()
            if lineas:
                ultima_linea = lineas[-1]
                ultimo_id = int(ultima_linea.split("&")[0])
            else:
                ultimo_id = 0
    except FileNotFoundError:
        ultimo_id = 0

    nuevo_id = ultimo_id + 1
    fecha_actual = datetime.now().strftime("%Y-%m-%d")
    leido = "False"
    cuerpo = confesion.replace("\n", "\\n")
    nueva_linea = f"{nuevo_id}&{cuerpo}&{fecha_actual}&{leido}\n"

    # Escribir la nueva línea
    with open("etc/secrets/confesiones.txt", "a", encoding="utf-8") as f:
        f.write(nueva_linea)
    print("Confesión guardada")
    