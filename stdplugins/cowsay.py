"""For .cowsay module, PepeBot wrapper for cow which says things.
    **⚠️🔞 NSFW WARNING**
   +++++CREDIT+++++++
   Code : @NeoMatrix90
   **Ported by @NeoMatrix90 (Ultra Legend)**
   Syntax : .cowsay {text} (cow will say dirty things. BE AWARE)
   		 .milksay {text} (A milk guy who hates cow)
   		 .tuxsay {text} (Find Out yourself)
   		 and many more, find out yourself, I iz Nub.
   		 
   ***#curse WHOEVER Change this, is a Gay and will be a Transgender, and cannot able to produce children. And he/she is a Bhosdiwala***
         ***🔴 DON'T COPY WITHOUT CREDIT***
         """
   
from telethon import events
from cowpy import cow

@borg.on(events.NewMessage(pattern=r"^.(\w+)say (.*)", outgoing=True))
async def univsaye(event):
    """ For .cowsay module, uniborg wrapper for cow which says things. """
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        arg = event.pattern_match.group(1).lower()
        text = event.pattern_match.group(2)

        if arg == "cow":
            arg = "default"
        if arg not in cow.COWACTERS:
            return
        cheese = cow.get_cow(arg)
        cheese = cheese()

        await event.edit(f"`{cheese.milk(text).replace('`', '´')}`")
