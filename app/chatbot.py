import logging

from discord.ext import commands

from .constants import DISCORD_TOKEN, client_ai, intents, init_db
from .commands import setup_commands
from .handlers import setup_event_handlers

try:
    from .constants import DISCORD_TOKEN, client_ai, intents, init_db
    from .commands import setup_commands
    from .handlers import setup_event_handlers
except ImportError:
    from constants import DISCORD_TOKEN, client_ai, intents, init_db
    from commands import setup_commands
    from handlers import setup_event_handlers


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

bot = commands.Bot(command_prefix="!", intents=intents)

init_db()
setup_commands(bot)
setup_event_handlers(bot, client_ai)

if __name__ == "__main__":
    bot.run(DISCORD_TOKEN)