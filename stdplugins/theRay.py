"""Emoji
Available Commands:
.ray"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "ray":

        await event.edit(input_str)

        animation_chars = [

            "RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy",
            
            "◼️RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁy",

            "◼️◼️RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RÀyRAyRÀyRAyRÁyRAyRÁy",

            "◼️◼️◼️️RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RÀyRAyRÀyRAy",

            "◼️◼️◼️◼️RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RÀyRAy",

            "‎◼️◼️◼️◼️◼️\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAy",

            "◼️◼️◼️◼️◼️\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀy",
            
            "◼️◼️◼️◼️◼️\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAy",
            
            "◼️◼️◼️◼️◼️\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRÀyRAyRÀy\RAyRÀyRAyRÀyRAy",
   
            "◼️◼️◼️◼️◼️\RAyRÀyRAyRÀyRAyRÁyRAyRÁy◼️\RAyRÀyRAyRÀyRAyRÁyRAyRÁy◼️\RAyRÀyRAyRÀyRAyRÁyRAyRÁy◼️\RAyRÀyRAyRÀyRAyRÁyRAyRÁyRA◼️",

            "◼️◼️◼️◼️◼️\yRÀyRAyRÀyRAyRÁyRAyRÁyRÀy◼️\RAyRÀyRAyRÀyRAyRÁyRAyRÁy◼️\RAyRÀyRAyRÀyRAyRÁyRAyRÁy◼️\RAyRÀyRAyRÀyRAyRÁyRA◼️◼️",

            "◼️◼️◼️◼️◼️\RAyRÀyRAyRÀyRAyRÁyRAyRAy◼️RAyRÀyRAyRÀyRAyRÁyRAyRAy\◼️\RAyRÀyRAyRÀyRAyRÁyRAyRAy◼️\RAyRÀyRAyRÀyRAy◼️◼️◼️",

            "◼️◼️◼️◼️◼️\yRÀyRAyRÀyRAyRÁyRAyRAy◼️\RAyRÀyRAyRÀyRAyRÁyRAyRAy◼️\RAyRÀyRAyRÀyRAyRÁyRAyRAy◼️\RAyRÀyRAyRA◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\AyRÀyRAyRÀyRAyRÁyRAyRAy◼️\RAyRÀyRAyRÀyRAyRÁyRAyRAy◼️\RAyRÀyRAyRÀyRAyRÁyRAyRAyRAy◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\RÀyRAyRÀyRAyRÁyRAyRAyRAy◼️\RÀyRAyRÀyRAyRÁyRAyRAyRAy◼️\R◼️RÀyRAyRÀyRAyRÁyRAy◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\RÀyRAyRÀyRAyRÁyRAyRAy◼️\R◼️RÀyRAyRÀyRAyRÁyRAyRAy◼️\R◼️RÀyRAyRÀyRAyRÁy◼️\R◼️◼️◼️◼️◼️",
            
            "◼️◼️◼️◼️◼️\R◼️RAyRAyRAyRAyRAyRAy◼️\R◼️RAyRAyRAyRAyRAyRAy◼️\R◼️RAyRAyRAyRAyR◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\R◼️◼️RAyRAyRAyRAyRAy◼️\R◼️RAyRAyRAyRAyRAy◼️\R◼️RAyRAyRAyRAy◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\R◼️◼️◼️RAyRAyRAyRAy◼️\R◼️RAyRAyRAyRAy◼️\R◼️RAyRAyRAyRAy◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️\R◼️RAyRAyRAyRAyRAy◼️\R◼️RAyRAyRAyRAyRAy◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️\R◼️RAyRAyRAyRAy◼️◼️\R◼️RAyRAyRAyRAyR◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️\R◼️RAyRAyRAy◼️◼️\R◼️RAyRAyRAyRA◼️◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️\R◼️RAyRAyRAy◼️◼️\R◼️RAVÁNÀ◼️◼️◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️\R◼️◼️RAyRAyRAy◼️◼️\R◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️\R◼️◼️RAyRAy◼️◼️\R◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️\R◼️◼️◼️◼️◼️",
          
            "◼️◼️◼️◼️\R◼️◼️◼️◼️\R◼️◼️◼️◼️\R◼️◼️◼️◼️",
           
            "◼️◼️◼️\R◼️◼️◼️\R◼️◼️◼️",

            "◼️◼️\R◼️◼️",

            "🔥"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])
