import os
import sys
import asyncio
from time import time
from datetime import datetime
from pyrogram import __version__, filters, Client
from pyrogram.types import Message
from platform import python_version
from ... import app, SUDO_USER
from ... import *

START_TIME = datetime.utcnow()
TIME_DURATION_UNITS = (
    ('Week', 60 * 60 * 24 * 7),
    ('Day', 60 * 60 * 24),
    ('Hour', 60 * 60),
    ('Min', 60),
    ('Sec', 1)
)
async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@app.on_message(cdz(["alive"])  & (filters.me | filters.user(SUDO_USER)))
async def alive(client: Client, message: Message):
    r = await message.reply_text("** #𝙵𝙴𝙴𝙻_4𝚂𝚃 **")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"︎ [ 😻 #𝙸_𝙼_𝙵4𝙴_𝙵𝚈𝚃𝙴𝚁 👻 ](https://t.me/II_4ST_PROFESSOR_READY_FOR_FUCKING_II) ︎︎︎\n\n"
        f"💌𝐕ᴇʀsɪᴏɴ ⁂1.0\n"
        f"💥𝐏ɪɴɢ ⁂ {ping * 1000:.3f}ᴍs\n"
        f"💭𝐔ᴘᴛɪᴍᴇ ⁂ {uptime}\n"
        f"💜𝐏ʏᴛʜᴏɴ ⁂ {python_version()}`\n"
        f"💓𝐏ʏʀᴏɢʀᴀᴍ ⁂ {__version__}\n"
        f"👑‌🇴𝐖𝐍𝐄𝐑💗 ⁂ {client.me.mention}"    
    )

@app.on_message(cdz(["ping"])  & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
    r = await message.reply_text("** #𝙵𝙴𝙴𝙻_4𝚂𝚃**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f" [ 😻 #𝚄𝚁_𝙳𝙰𝙳𝙳𝚈_𝙵4𝙴_𝙰𝚄𝚃𝙸𝚂𝚃𝙸𝙲_𝙷𝙴𝚁𝙴 👻 ](https://t.me/II_4ST_PROFESSOR_READY_FOR_FUCKING_II) \n\n"
        f"🌐➍ˢᵀ 𝐏𝙸𝙽𝙶 ❄  ⁂ {ping * 1000:.3f}ᴍs\n"
        f"‌‌👑🇸𝐔𝐏𝐄𝐑 ‌🇴𝐖𝐍𝐄𝐑 💕  ⁂ {client.me.mention}\n"
        f"⚡🇹𝐈𝐌𝐄 🔥 ⁂ {uptime}\n"
              )
@app.on_message(cdz(["repo"])  & (filters.me | filters.user(SUDO_USER)))
async def ping(client: Client, message: Message):
    r = await message.reply_text("**𝐑ᴇᴘᴏ**")
    start = time()
    current_time = datetime.utcnow()
    ping = time() - start
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.delete()
    await r.edit(
        f"𝗥𝗘𝗣𝗢 ⁂\n\n"
        f"[💫 𝐑ᴇᴘᴏ 💫](https://t.me/Fakecheater77x/PROFESSOR_PYTHON)\n"
    )    


__NAME__ = " Aᴄᴛɪᴠᴇ "
__MENU__ = """
`.ping` - **Check Ping Latency
Of Your Userbot Server.**

`.alive` - **Check Ping Latency
Of Your Userbot Server.**

`.repo` - **chek bot repo.**
"""
