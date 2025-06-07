from variables import SB_URL, SB_KEY
from supabase import create_client, Client

supabase: Client = create_client(SB_URL, SB_KEY)

def guardarConfesión(cuerpo: str, fecha: str, leido: bool):
    nuevo = {"cuerpo": cuerpo, "fecha": fecha, "leido": leido}
    supabase.table("confesion").insert(nuevo).execute()