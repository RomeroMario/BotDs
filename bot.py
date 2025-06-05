import discord
from discord.ext import commands
from modals import ConfessModal

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"🤖 Bot conectado como {bot.user}. Preparado")

@bot.slash_command(name="ping", description="Verifica si el bot está activo")
async def ping(ctx: discord.ApplicationContext):
    print("ping")
    await ctx.send_response("Pong!")
    
@bot.slash_command(name="confesion")
async def confesion(ctx: discord.ApplicationContext):
    await ctx.interaction.response.send_modal(ConfessModal())
    
@bot.slash_command(name="mago",description="Pasa algo mágico")
async def mago(ctx: discord.ApplicationContext):
    await ctx.send_response("Sos el magodito jijijijijijijijii", ephemeral=True)