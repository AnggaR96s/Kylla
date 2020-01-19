from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern="ping ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    mole = await event.reply("🇵 🇴 🇳 🇬 \n👇")
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await mole.edit("`🇵 🇴 🇳 🇬 👇`\n`{}ms`".format(ms))
