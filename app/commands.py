from typing import Optional

import discord
from discord import app_commands

from .personas import channel_personas, save_channel_personas, delete_channel_persona
from .model import channel_models

persona_group = app_commands.Group(
    name="persona",
    description="人格設定"
)
@persona_group.command(
    name="show",
    description="現在の人格設定を表示"
)
async def persona_show(
    interaction: discord.Interaction
):
    current = channel_personas.get(
        interaction.channel_id
    )
    if current is None:
        current = "なし"
    await interaction.response.send_message(
        f"現在の人格: {current}", ephemeral=True
    )

@persona_group.command(
    name="set",
    description="新しい人格に変更"
)
@app_commands.choices(
    persona=[
        app_commands.Choice(name="全員", value="全員"),
        app_commands.Choice(name="みさき", value="みさき"),
        app_commands.Choice(name="あや", value="あや"),
        app_commands.Choice(name="りん", value="りん"),
        app_commands.Choice(name="ゆい", value="ゆい"),
        app_commands.Choice(name="なぎさ", value="なぎさ"),
        app_commands.Choice(name="ことね", value="ことね"),
    ]
)
async def persona_set(
    interaction: discord.Interaction,
    persona: app_commands.Choice[str],
):
    channel_personas[interaction.channel_id] = persona.value
    save_channel_personas(
        interaction.channel_id,
        persona.value
    )
    await interaction.response.send_message(
        f"人格を {persona.value} に変更しました。", ephemeral=True
    )

@persona_group.command(
    name="clear",
    description="人格設定を解除"
)
async def persona_clear(
    interaction: discord.Interaction
):
    channel_personas.pop(interaction.channel_id, None)
    delete_channel_persona(
        interaction.channel_id
    )
    await interaction.response.send_message("人格設定を解除しました。", ephemeral=True)
    return

def setup_commands(bot):
    bot.tree.add_command(
        persona_group
    )
