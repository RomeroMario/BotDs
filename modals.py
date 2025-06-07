import discord
from variables import cola
from api import save_confess


class ConfessModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Confesiones")
        self.add_item(
            discord.ui.InputText(
                label="CONFIESA, tú quien no conoce la verguenza",
                required=True,
                style=discord.InputTextStyle.long,
                max_length=450,
                placeholder="No sé como golpear al nexo. Atte: Elucho"
            )
        )

    async def callback(self, interaction: discord.Interaction):
        await save_confess(self.children[0].value)
        await interaction.response.send_message(
            f"Confesión guardada  {cola}", ephemeral=True
        )
        
class SorteoModal(discord.ui.Modal):
    def __init__(self):
        super().__init__(title="Sorteo de Participantes")
        self.add_item(
            discord.ui.InputText(
                label="Escribe un participante por línea",
                style=discord.InputTextStyle.long,
                required=True,
                placeholder="Ejemplo:\nJuan\nAna\nPedro"
            )
        )

    async def callback(self, interaction: discord.Interaction):
        texto = self.children[0].value
        participantes = [p.strip() for p in texto.splitlines() if p.strip()]
        if not participantes:
            await interaction.response.send_message("No se ingresaron participantes.", ephemeral=True)
            return
        import random
        import asyncio
        ganador = random.choice(participantes)
        lista = "\n".join(f"- {p}" for p in participantes)
        await interaction.response.send_message(f"🎲 **Participantes:**\n{lista}", ephemeral=False)
        await interaction.followup.send(f"🏆 **Ganador:** {ganador}", ephemeral=False)
        msg = await interaction.followup.send("🎰 Girando la ruleta...", ephemeral=False)
        
        for _ in range(30):
            seleccionado = random.choice(participantes)
            await msg.edit(content=f"🎰 Girando la ruleta...\n> {seleccionado}")
            await asyncio.sleep(0.25)

        ganador = random.choice(participantes)
        await msg.edit(content=f"🏆 **¡Ganador/a!**\n> {ganador}")