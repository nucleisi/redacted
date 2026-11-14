import os
import re

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

IM_PATTERN = re.compile(
    r"\b(?:i['’]?m|i am)\s+(.+?)\s*(?:[.,!?;\n]|$)",
    re.IGNORECASE,
)

MAX_NICK_LENGTH = 32 


@client.event
async def on_ready():
    print(f"logged in as {client.user} (id: {client.user.id})")


@client.event
async def on_message(message: discord.Message):
    if message.author.bot or message.guild is None:
        return

    match = IM_PATTERN.search(message.content)
    if not match:
        return

    new_nick = match.group(1).strip()[:MAX_NICK_LENGTH]
    if not new_nick:
        return

    try:
        await message.author.edit(nick=new_nick, reason="they said 'i'm ...'")
    except discord.Forbidden:
        print(f"can't rename {message.author} (missing permission or role too high)")
        return
    except discord.HTTPException as e:
        print(f"failed to rename {message.author}: {e}")
        return

    await message.channel.send(
        f"hi {new_nick}, i'm {client.user.display_name}",
        allowed_mentions=discord.AllowedMentions.none(),
    )


client.run(TOKEN)
