import discord
from discord.ext import commands
from modals import ConfessModal,SorteoModal

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"🤖 Bot conectado como {bot.user}. Preparado")
    
@bot.event
async def on_message(message):
    canal_objetivo = 1380371553887191040  # Reemplaza con el ID de tu canal
    if message.channel.id == canal_objetivo and not message.author.bot:
        await message.delete()
    await bot.process_commands(message)

@bot.slash_command(name="ping", description="Verifica si el bot está activo")
async def ping(ctx: discord.ApplicationContext):
    print("ping")
    await ctx.send_response("Pong!")
    
@bot.slash_command(name="confesion", description="Usa el comando y LUEGO escribí la confesión")
async def confesion(ctx: discord.ApplicationContext):
    await ctx.interaction.response.send_modal(ConfessModal())
    
@bot.slash_command(name="sorteo", description="Escribe opciones para sortear")
async def sorteo(ctx: discord.ApplicationContext):
    await ctx.interaction.response.send_modal(SorteoModal())
    
@bot.slash_command(name="mago",description="Pasa algo mágico")
async def mago(ctx: discord.ApplicationContext):
    await ctx.send_response("Sos el magodito jijijijijijijijii", ephemeral=True)