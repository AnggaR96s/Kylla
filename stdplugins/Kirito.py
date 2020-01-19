"""Emoji
Available Commands:
.kirito"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.3

    animation_ttl = range(0, 30)

    input_str = event.pattern_match.group(1)

    if input_str == "kirito":

        await event.edit(input_str)

        animation_chars = [

            "😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️️😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️◼️😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "‎◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️\n◼️😈kirito, Eyepatch😈◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️😈kirito, Eyepatch😈😈kirito, Eyepatch😈◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️😈kirito, Eyepatch😈◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️",

            "◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️",

            "◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️",

            "◼️◼️\n◼️◼️",

            "◼️"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 30])
