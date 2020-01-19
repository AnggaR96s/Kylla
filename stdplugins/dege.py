"""Fun Pligon For @PepeBot
\nCode By © [Eyepatch](https://t.me/NeoMatrix90)
\nType .nehi to see the fun.
"""

from telethon import events
import asyncio
import os
import sys
import random
@borg.on(events.NewMessage(pattern=r"\.nehi", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("`Wo PaKkA DeGi Tu ManG KaR ToH DekH`")
    await asyncio.sleep(999)