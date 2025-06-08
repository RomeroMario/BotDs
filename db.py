from variables import SB_URL, SB_KEY
from supabase import create_client, Client

supabase: Client = create_client(SB_URL, SB_KEY)


def obtenerConfesiones():
    data = supabase.table("confesion").select("*").order("id", desc=False).execute()
    return data.data

def guardarConfesión(cuerpo: str, fecha: str, leido: bool):
    nuevo = {"cuerpo": cuerpo, "fecha": fecha, "estado": leido}
    supabase.table("confesion").insert(nuevo).execute()
    
def modificarEstado(id: int):
    # Obtener la confesión actual
    res = supabase.table("confesion").select("estado").eq("id", id).single().execute()
    if not res.data:
        return  # No existe esa confesión

    estado_actual = res.data["estado"]
    nuevo_estado = not estado_actual

    # Actualizar el estado en la base de datos
    supabase.table("confesion").update({"estado": nuevo_estado}).eq("id", id).execute()