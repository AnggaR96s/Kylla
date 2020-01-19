"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 2

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "netflix":

        await event.edit(input_str)

        animation_chars = [
        
            "`Cracking some Netflix account.....`",
           
            "`Cracking ... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Cracking... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Cracking... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",    
            "`Cracking... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Cracking... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Cracking... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
            "`Cracking... 84%\n█████████████████████▒▒▒▒ `",
        "`Cracked... 100%\n█████████Cracked ███████████ `",
        "`I'd :- *************@gmail.com\n\nPassword:-**********`",   

 "`Account Cracked ..\n\n Pay 2$ to @kirito6969 for I'd and Password`"
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])
