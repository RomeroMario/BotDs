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