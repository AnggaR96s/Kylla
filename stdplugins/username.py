"""Plugin To Change Username by @Refundisillegal and the Help of @SpEcHiDe
Available Commands:
.usr <Username>"""


from uniborg.util import admin_cmd
from telethon.errors.rpcerrorlist import UsernameOccupiedError, UsernameInvalidError
from telethon.tl.functions.account import UpdateUsernameRequest


@borg.on(admin_cmd(pattern="usr ?(.*)"))
async def update_username(username):
    newusername = username.pattern_match.group(1)
    if newusername.startswith("@"):
        newusername = newusername[1:]
    try:
        await borg(UpdateUsernameRequest(newusername))
        
        await username.edit("Succesfully changed my Username")
    except UsernameOccupiedError:
        await event.edit("This Username is Already Reserved")

        
