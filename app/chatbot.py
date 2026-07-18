import logging

from discord.ext import commands

from .constants import DISCORD_TOKEN, client_ai, intents
from .commands import setup_commands
from .handlers import setup_event_handlers
from .db import init_db
from .personas import channel_personas, load_channel_personas

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

bot = commands.Bot(command_prefix="!", intents=intents)

setup_commands(bot)
setup_event_handlers(bot, client_ai)

init_db()
channel_personas.update(
    load_channel_personas()
)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)