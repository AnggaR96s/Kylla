"""use cmd .nikita
aaahaaa you can edit this 😉"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "nikita":

        await event.edit(input_str)

        animation_chars = [

            "👑Nikita👑👑👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",

            "◼️👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",

            "◼️◼️👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",

            "◼️◼️◼️️👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",

            "◼️◼️◼️◼️👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",

            "‎◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",

            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",

            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",

            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑",

            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️",

            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n👑Nikita👑👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑◼️◼️\n◼️👑Nikita👑👑Nikita👑👑Nikita👑◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑◼️◼️\n◼️👑Nikita👑👑Nikita👑◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑◼️◼️\n◼️👑Nikita👑◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️👑Nikita👑👑Nikita👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️👑Nikita👑◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️",
            "👑 Nikita 👑"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 31])
