""".ipromote\
\nUsage: Reply to someone's message with .promote to promote them.\
\n\n.idemote\
\nUsage: Reply to someone's message with .demote to revoke their admin permissions.\
\n\n.iban\
\nUsage: Reply to someone's message with .ban to ban them.\
\n\n.iunban\
\nUsage: Reply to someone's message with .unban to unban them in this chat.\
\n\n.imute\
\nUsage: Reply to someone's message with .mute to mute them, works on admins too.\
\n\n.iunmute\
\nUsage: Reply to someone's message with .unmute to remove them from muted list.\
\n\n.igmute\
\nUsage: Reply to someone's message with .gmute to mute them in all groups you have in common with them.\
\n\n.iungmute\
\nUsage: Reply someone's message with .ungmute to remove them from the gmuted list.\
\n\n.idelusers\
\nUsage: Searches for deleted accounts in a group. Use .delusers clean to remove deleted accounts from the group.\
\n\n.iadminlist\
\nUsage: Retrieves all admins in a chat.\
\n\n.iuserslist or .userslist <name>\
\nUsage: Retrieves all users in a chat.
\n\n.iundlt\
\nUsage: Sends the last deleted message in group."

Userbot module to help you manage a group.
  © [cHAuHaN](http://t.me/amnd33p)"""

from asyncio import sleep
from os import remove
from telethon import events
from uniborg.util import admin_cmd
from telethon.errors import (BadRequestError, ChatAdminRequiredError,
                             ImageProcessFailedError, PhotoCropSizeSmallError,
                             UserAdminInvalidError)
from telethon.errors.rpcerrorlist import (UserIdInvalidError,
                                          MessageTooLongError)
from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)
from telethon.tl.functions.messages import UpdatePinnedMessageRequest
from telethon.tl.types import (ChannelParticipantsAdmins, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto, PeerChat)
ENABLE_LOG = True
LOGGING_CHATID = Config.PRIVATE_CHANNEL_BOT_API_ID
BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)
UNBAN_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=None,
    send_media=None,
    send_stickers=None,
    send_gifs=None,
    send_games=None,
    send_inline=None,
    embed_links=None,
)
KICK_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True
)
MUTE_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=True
)
UNMUTE_RIGHTS = ChatBannedRights(
    until_date=None,
    send_messages=False
)

@borg.on(events.NewMessage(outgoing=True, pattern="^.setgic$"))
async def setgrouppic(eventPic):
    if not eventPic.text[0].isalpha() and eventPic.text[0] not in ("/", "#", "@", "!"):
        if eventPic.reply_to_msg_id:
            replymsg = await eventPic.get_reply_message()
            chat = await eventPic.get_chat()
            admin = chat.admin_rights
            creator = chat.creator
            photo = None
            if not admin and not creator:
                await eventPic.edit("`I am not an admin!`")
                return
            if replymsg and replymsg.media:
                if isinstance(replymsg.media, MessageMediaPhoto):
                    photo = await eventPic.client.download_media(message=replymsg.photo)
                elif "image" in replymsg.media.document.mime_type.split('/'):
                    photo = await eventPic.client.download_file(replymsg.media.document)
                else:
                    await eventPic.edit("`Invalid Extension`")
            if photo:
                try:
                    await eventPic.client(EditPhotoRequest(
                    eventPic.chat_id,
                    await eventPic.client.upload_file(photo)
                    ))
                    await eventPic.edit("`Chat Picture Changed`")

                except PhotoCropSizeSmallError:
                    await eventPic.edit("`The image is too small`")
                except ImageProcessFailedError:
                    await eventPic.edit("`Failure while processing the image`")
        else:
            await eventPic.edit("`Reply .setgrouppic to an Image to set it as group's icon.`")


@borg.on(events.NewMessage(outgoing=True, pattern="^.ipromote(?: |$)(.*)"))
async def promote(eventPromote):
    if not eventPromote.text[0].isalpha() \
            and eventPromote.text[0] not in ("/", "#", "@", "!"):
        chat = await eventPromote.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventPromote.edit("`I am not an admin!`")
            return
        newAdminRights = ChatAdminRights(
            add_admins=False,
            invite_users=True,
            change_info=False,
            ban_users=True,
            delete_messages=True,
            pin_messages=True
        )
        await eventPromote.edit("`Promoting this guy...`")
        user = await get_user_from_event(eventPromote)
        if user:
            pass
        else:
            return
        try:
            await eventPromote.client(
                EditAdminRequest(
                    eventPromote.chat_id,
                    user.id,
                    newAdminRights,
                    rank = ""
                )
            )
            await eventPromote.edit("`Promoted Successfully!`")
        except BadRequestError:
            await eventPromote.edit("`I don't have sufficient permissions!`")
            return
        if ENABLE_LOG:
            await eventPromote.client.send_message(
                LOGGING_CHATID,
                "#PROMOTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {eventPromote.chat.title}(`{eventPromote.chat_id}`)"
            )


@borg.on(events.NewMessage(outgoing=True, pattern="^.idemote(?: |$)(.*)"))
async def demote(eventDemote):
    if not eventDemote.text[0].isalpha() and eventDemote.text[0] not in ("/", "#", "@", "!"):
        chat = await eventDemote.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventDemote.edit("`I am not an admin!`")
            return
        await eventDemote.edit("`Demoting...`")
        user = await get_user_from_event(eventDemote)
        if user:
            pass
        else:
            return
        newAdminRights = ChatAdminRights(
            add_admins=None,
            invite_users=None,
            change_info=None,
            ban_users=None,
            delete_messages=None,
            pin_messages=None
        )
        try:
            await eventDemote.client(
                EditAdminRequest(
                    eventDemote.chat_id,
                    user.id,
                    newAdminRights,
                    rank = ""
                )
            )
        except BadRequestError:
            await eventDemote.edit("`I don't have sufficient permissions!`")
            return
        await eventDemote.edit("`Demoted Successfully!`")
        if ENABLE_LOG:
            await eventDemote.client.send_message(
                LOGGING_CHATID,
                "#DEMOTE\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {eventDemote.chat.title}(`{eventDemote.chat_id}`)"
            )


@borg.on(events.NewMessage(outgoing=True, pattern="^.iban(?: |$)(.*)"))
async def ban(eventBan):
    if not eventBan.text[0].isalpha() and eventBan.text[0] not in ("/", "#", "@", "!"):
        chat = await eventBan.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventBan.edit("`I am not an admin!`")
            return
        user = await get_user_from_event(eventBan)
        if user:
            pass
        else:
            return
        await eventBan.edit("`Finding this retarded guy...`")
        try:
            await eventBan.client(
                EditBannedRequest(
                    eventBan.chat_id,
                    user.id,
                    BANNED_RIGHTS
                )
            )
        except BadRequestError:
            await eventBan.edit("`I don't have sufficient permissions!`")
            return
        try:
            reply = await eventBan.get_reply_message()
            if reply:
                await reply.delete()
        except BadRequestError:
            await eventBan.edit("`I dont have message nuking rights! But still he was banned!`")
            return
        await eventBan.edit("`{}` was banned!".format(str(user.id)))
        if ENABLE_LOG:
            await eventBan.client.send_message(
                LOGGING_CHATID,
                "#BAN\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {eventBan.chat.title}(`{eventBan.chat_id}`)"
            )


@borg.on(events.NewMessage(outgoing=True, pattern="^.bots$"))
async def listbots(eventListBots):
    info = await eventListBots.client.get_entity(eventListBots.chat_id)
    title = info.title if info.title else "this chat"
    mentions = f'<b>Bots in {title}:</b>\n'
    try:
        if isinstance(eventListBots.to_id, PeerChat):
            await eventListBots.edit("`Only Supergroups can have bots.`")
            return
        else:
            async for user in eventListBots.client.iter_participants(
                    eventListBots.chat_id, filter=ChannelParticipantsBots):
                if not user.deleted:
                    link = f"<a href=\"tg://user?id={user.id}\">{user.first_name}</a>"
                    userid = f"<code>{user.id}</code>"
                    mentions += f"\n{link} {userid}"
                else:
                    mentions += f"\n<code>{user.id}</code>(Bot deleted by owner)"
    except ChatAdminRequiredError as err:
        mentions += " " + str(err) + "\n"
    try:
        await eventListBots.edit(mentions, parse_mode="html")
    except MessageTooLongError:
        await eventListBots.edit(
            "This group is filled with bots as hell. Uploading bots list as file.")
        file = open("botlist.txt", "w+")
        file.write(mentions)
        file.close()
        await eventListBots.client.send_file(
            eventListBots.chat_id,
            "botlist.txt",
            caption='Bots in {}'.format(title),
            reply_to=eventListBots.id,
        )
        remove("botlist.txt")
            
@borg.on(events.NewMessage(outgoing=True, pattern="^.iunban(?: |$)(.*)"))
async def unban(eventUnban):
    if not eventUnban.text[0].isalpha() and eventUnban.text[0] \
            not in ("/", "#", "@", "!"):
        chat = await eventUnban.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventUnban.edit("`I am not an admin!`")
            return
        await eventUnban.edit("[cHAuHaN](http://t.me/amnd33p) `forgives everyone. Unbanning!`")
        user = await get_user_from_event(eventUnban)
        if user:
            pass
        else:
            return
        try:
            await eventUnban.client(EditBannedRequest(
                eventUnban.chat_id,
                user.id,
                UNBAN_RIGHTS
            ))
            await eventUnban.edit("```Unbanned Successfully```")
            if ENABLE_LOG:
                await eventUnban.client.send_message(
                    LOGGING_CHATID,
                    "#UNBAN\n"
                    f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                    f"CHAT: {eventUnban.chat.title}(`{eventUnban.chat_id}`)"
                )
        except UserIdInvalidError:
            await eventUnban.edit("`Uh oh my unban logic broke!`")


@borg.on(events.NewMessage(outgoing=True, pattern="^.imute(?: |$)(.*)"))
async def mute(eventMute):
    if not eventMute.text[0].isalpha() and eventMute.text[0] not in ("/", "#", "@", "!"):
        try:
            from sql_helpers.spam_mute_sql import mute
        except AttributeError:
            await eventMute.edit("`Running on Non-SQL mode!`")
            return
        chat = await eventMute.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventMute.edit("`I am not an admin!`")
            return

        user = await get_user_from_event(eventMute)
        if user:
            pass
        else:
            return
        self_user = await eventMute.client.get_me()
        if user.id == self_user.id:
            await eventMute.edit("`Hands too short, can't duct tape myself...\n(ヘ･_･)ヘ┳━┳`")
            return
        await eventMute.edit("`Gets a tape!`")
        if mute(eventMute.chat_id, user.id) is False:
            return await eventMute.edit('`Error! User probably already muted.`')
        else:
            try:
                await eventMute.client(
                    EditBannedRequest(
                        eventMute.chat_id,
                        user.id,
                        MUTE_RIGHTS
                    )
                )
                await eventMute.edit("`Safely taped!`")
                if ENABLE_LOG:
                    await eventMute.client.send_message(
                        LOGGING_CHATID,
                        "#MUTE\n"
                        f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                        f"CHAT: {eventMute.chat.title}(`{eventMute.chat_id}`)"
                    )
            except UserIdInvalidError:
                return await eventMute.edit("`Uh oh my mute logic broke!`")


@borg.on(events.NewMessage(outgoing=True, pattern="^.iunmute(?: |$)(.*)"))
async def unmute(eventUnMute):
    if not eventUnMute.text[0].isalpha() and eventUnMute.text[0] \
            not in ("/", "#", "@", "!"):
        chat = await eventUnMute.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventUnMute.edit("`I am not an admin!`")
            return
        try:
            from sql_helpers.spam_mute_sql import unmute
        except AttributeError:
            await eventUnMute.edit("`Running on Non-SQL mode!`")
            return
        await eventUnMute.edit('```Unmuting...```')
        user = await get_user_from_event(eventUnMute)
        if user:
            pass
        else:
            return
        if unmute(eventUnMute.chat_id, user.id) is False:
            return await eventUnMute.edit("`Error! User probably already unmuted.`")
        else:

            try:
                await eventUnMute.client(
                    EditBannedRequest(
                        eventUnMute.chat_id,
                        user.id,
                        UNBAN_RIGHTS
                    )
                )
                await eventUnMute.edit("```Unmuted Successfully```")
            except UserIdInvalidError:
                await eventUnMute.edit("`Uh oh my unmute logic broke!`")
                return

            if ENABLE_LOG:
                await eventUnMute.client.send_message(
                    LOGGING_CHATID,
                    "#UNMUTE\n"
                    f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                    f"CHAT: {eventUnMute.chat.title}(`{eventUnMute.chat_id}`)"
                )


@borg.on(events.NewMessage(incoming=True))
async def muter(mutedMessage):
    try:
        from sql_helpers.spam_mute_sql import is_muted
        from sql_helpers.gmute_sql import is_gmuted
    except AttributeError:
        return
    muted = is_muted(mutedMessage.chat_id)
    gmuted = is_gmuted(mutedMessage.sender_id)
    rights = ChatBannedRights(
        until_date=None,
        send_messages=True,
        send_media=True,
        send_stickers=True,
        send_gifs=True,
        send_games=True,
        send_inline=True,
        embed_links=True,
    )
    if muted:
        for i in muted:
            if str(i.sender) == str(mutedMessage.sender_id):
                await mutedMessage.delete()
                await mutedMessage.client(EditBannedRequest(
                    mutedMessage.chat_id,
                    mutedMessage.sender_id,
                    rights
                ))
    for i in gmuted:
        if i.sender == str(mutedMessage.sender_id):
            await mutedMessage.delete()


@borg.on(events.NewMessage(outgoing=True, pattern="^.igmute(?: |$)(.*)"))
async def gmute(eventGmute):
    if not eventGmute.text[0].isalpha() and eventGmute.text[0] not in ("/", "#", "@", "!"):
        chat = await eventGmute.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventGmute.edit("`I am not an admin!`")
            return
        try:
            from sql_helpers.gmute_sql import gmute
        except AttributeError:
            await eventGmute.edit("`Running on Non-SQL mode!`")
            return

        user = await get_user_from_event(eventGmute)
        if user:
            pass
        else:
            return
        await eventGmute.edit("`Grabs a huge, sticky duct tape!`")
        if gmute(user.id) is False:
            await eventGmute.edit('`Error! User probably already gmuted.\nRe-rolls the tape.`')
        else:
            await eventGmute.edit("`Haha Yash! Globally taped!`")

            if ENABLE_LOG:
                await eventGmute.client.send_message(
                    LOGGING_CHATID,
                    "#GMUTE\n"
                    f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                    f"CHAT: {eventGmute.chat.title}(`{eventGmute.chat_id}`)"
                )


@borg.on(events.NewMessage(outgoing=True, pattern="^.iungmute(?: |$)(.*)"))
async def ungmute(eventUnGmute):
    if not eventUnGmute.text[0].isalpha() and eventUnGmute.text[0] \
            not in ("/", "#", "@", "!"):
        chat = await eventUnGmute.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventUnGmute.edit("`I am not an admin!`")
            return
        try:
            from sql_helpers.gmute_sql import ungmute
        except AttributeError:
            await eventUnGmute.edit("`Running on Non-SQL mode!`")
            return
        user = await get_user_from_event(eventUnGmute)
        if user:
            pass
        else:
            return
        await eventUnGmute.edit('```Ungmuting...```')

        if ungmute(user.id) is False:
            await eventUnGmute.edit("`Error! User probably not gmuted.`")
        else:
            await eventUnGmute.edit("```Ungmuted Successfully```")

            if ENABLE_LOG:
                await eventUnGmute.client.send_message(
                    LOGGING_CHATID,
                    "#UNGMUTE\n"
                    f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                    f"CHAT: {eventUnGmute.chat.title}(`{eventUnGmute.chat_id}`)"
                )


@borg.on(events.NewMessage(outgoing=True, pattern="^.idelusers(?: |$)(.*)"))
async def rm_deletedacc(eventDeletedAccs):
    if not eventDeletedAccs.text[0].isalpha() and eventDeletedAccs.text[0] not in ("/", "#", "@", "!"):
        con = eventDeletedAccs.pattern_match.group(1)
        del_u = 0
        del_status = "`No deleted accounts found, Group is cleaned as Hell`"

        if not eventDeletedAccs.is_group:
            await eventDeletedAccs.edit("`This command is only for groups!`")
            return
        if con != "clean":
            await eventDeletedAccs.edit("`Searching for ded af accounts...`")
            async for user in eventDeletedAccs.client.iter_participants(
                    eventDeletedAccs.chat_id
            ):
                if user.deleted:
                    del_u += 1

            if del_u > 0:
                del_status = f"found **{del_u}** deleted account(s) in this group \
                \nClean them by using .delusers clean"
            await eventDeletedAccs.edit(del_status)
            return
        chat = await eventDeletedAccs.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventDeletedAccs.edit("`I am not an admin here!`")
            return
        await eventDeletedAccs.edit("`Deleting deleted accounts...\nOh I can do that?!?!`")
        del_u = 0
        del_a = 0
        async for user in eventDeletedAccs.client.iter_participants(
                eventDeletedAccs.chat_id
        ):
            if user.deleted:
                try:
                    await eventDeletedAccs.client(
                        EditBannedRequest(
                            eventDeletedAccs.chat_id,
                            user.id,
                            BANNED_RIGHTS
                        )
                    )
                except ChatAdminRequiredError:
                    await eventDeletedAccs.edit("`I don't have ban rights in this group`")
                    return
                except UserAdminInvalidError:
                    del_u -= 1
                    del_a += 1
                await eventDeletedAccs.client(
                    EditBannedRequest(
                        eventDeletedAccs.chat_id,
                        user.id,
                        UNBAN_RIGHTS
                    )
                )
                del_u += 1
        if del_u > 0:
            del_status = f"Cleaned **{del_u}** deleted account(s)"
        if del_a > 0:
            del_status = f"Cleaned **{del_u}** deleted account(s) \
            \n**{del_a}** deleted admin accounts are not removed."
        await eventDeletedAccs.edit(del_status)


@borg.on(events.NewMessage(outgoing=True, pattern="^.iadminlist$"))
async def listadmins(eventListAdmins):
    if not eventListAdmins.text[0].isalpha() and eventListAdmins.text[0] not in ("/", "#", "@", "!"):
        if not eventListAdmins.is_group:
            await eventListAdmins.edit("I don't think this is a group.")
            return
        info = await eventListAdmins.client.get_entity(eventListAdmins.chat_id)
        title = info.title if info.title else "this chat"
        mentions = f'<b>Admins in {title}:</b> \n'
        try:
            async for user in eventListAdmins.client.iter_participants(
                    eventListAdmins.chat_id, filter=ChannelParticipantsAdmins
            ):
                if not user.deleted:
                    link = f"<a href=\"tg://user?id={user.id}\">{user.first_name}</a>"
                    userid = f"<code>{user.id}</code>"
                    mentions += f"\n{link} {userid}"
                else:
                    mentions += f"\nDeleted Account <code>{user.id}</code>"
        except ChatAdminRequiredError as err:
            mentions += " " + str(err) + "\n"
        await eventListAdmins.edit(mentions, parse_mode="html")


@borg.on(events.NewMessage(outgoing=True, pattern="^.ipin(?: |$)(.*)"))
async def pinmessage(eventPinMessage):
    if not eventPinMessage.text[0].isalpha() and eventPinMessage.text[0] not in ("/", "#", "@", "!"):
        chat = await eventPinMessage.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventPinMessage.edit("`I am not an admin!`")
            return
        to_pin = eventPinMessage.reply_to_msg_id
        if not to_pin:
            await eventPinMessage.edit("`Reply to a message to pin it.`")
            return
        options = eventPinMessage.pattern_match.group(1)
        is_silent = True
        if options.lower() == "loud":
            is_silent = False
        try:
            await eventPinMessage.client(UpdatePinnedMessageRequest(eventPinMessage.to_id, to_pin, is_silent))
        except BadRequestError:
            await eventPinMessage.edit("`I don't have sufficient permissions!`")
            return
        await eventPinMessage.edit("`Pinned Successfully!`")
        user = await get_user_from_id(eventPinMessage.from_id, eventPinMessage)
        if ENABLE_LOG:
            await eventPinMessage.client.send_message(
                LOGGING_CHATID,
                "#PIN\n"
                f"ADMIN: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {eventPinMessage.chat.title}(`{eventPinMessage.chat_id}`)\n"
                f"LOUD: {not is_silent}"
            )


@borg.on(events.NewMessage(outgoing=True, pattern="^.ikick(?: |$)(.*)"))
async def kick(eventKickUser):
    if not eventKickUser.text[0].isalpha() and eventKickUser.text[0] not in ("/", "#", "@", "!"):
        chat = await eventKickUser.get_chat()
        admin = chat.admin_rights
        creator = chat.creator
        if not admin and not creator:
            await eventKickUser.edit("`I am not an admin!`")
            return
        user = await get_user_from_event(eventKickUser)
        if not user:
            await eventKickUser.edit("`Couldn't fetch user.`")
            return
        await eventKickUser.edit("`Kicking this nibba...`")
        try:
            await eventKickUser.client(
                EditBannedRequest(
                    eventKickUser.chat_id,
                    user.id,
                    KICK_RIGHTS
                )
            )
            await sleep(.5)
        except BadRequestError:
            await eventKickUser.edit("`I don't have sufficient permissions!`")
            return
        await eventKickUser.client(
            EditBannedRequest(
                eventKickUser.chat_id,
                user.id,
                ChatBannedRights(until_date=None)
            )
        )
        await eventKickUser.edit(f"`Kicked` [{user.first_name}](tg://user?id={user.id})`!`")
        if ENABLE_LOG:
            await eventKickUser.client.send_message(
                LOGGING_CHATID,
                "#KICK\n"
                f"USER: [{user.first_name}](tg://user?id={user.id})\n"
                f"CHAT: {eventKickUser.chat.title}(`{eventKickUser.chat_id}`)\n"
            )


@borg.on(events.NewMessage(outgoing=True, pattern="^.iuserslist ?(.*)"))
async def list_users(eventListUsers):
    if not eventListUsers.text[0].isalpha() and eventListUsers.text[0] not in ("/", "#", "@", "!"):
        if not eventListUsers.is_group:
            await eventListUsers.edit("Are you sure this is a group?")
            return
        info = await eventListUsers.client.get_entity(eventListUsers.chat_id)
        title = info.title if info.title else "this chat"
        mentions = 'Users in {}: \n'.format(title)
        try:
            if not eventListUsers.pattern_match.group(1):
                async for user in eventListUsers.client.iter_participants(eventListUsers.chat_id):
                    if not user.deleted:
                        mentions += f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                    else:
                        mentions += f"\nDeleted Account `{user.id}`"
            else:
                searchq = eventListUsers.pattern_match.group(1)
                async for user in eventListUsers.client.iter_participants(eventListUsers.chat_id, search=f'{searchq}'):
                    if not user.deleted:
                        mentions += f"\n[{user.first_name}](tg://user?id={user.id}) `{user.id}`"
                    else:
                        mentions += f"\nDeleted Account `{user.id}`"
        except ChatAdminRequiredError as err:
            mentions += " " + str(err) + "\n"
        try:
            await eventListUsers.edit(mentions)
        except MessageTooLongError:
            await eventListUsers.edit("Damn, this is a huge group. Uploading users lists as file.")
            file = open("userslist.txt", "w+")
            file.write(mentions)
            file.close()
            await eventListUsers.client.send_file(
                eventListUsers.chat_id,
                "userslist.txt",
                caption='Users in {}'.format(title),
                reply_to=eventListUsers.id,
            )
            remove("userslist.txt")

@borg.on(admin_cmd(pattern="iundlt$"))
async def _(event):
    if event.fwd_from:
        return
    c = await event.get_chat()
    if c.admin_rights or c.creator:
        a = await borg.get_admin_log(event.chat_id,limit=1, search="", edit=False, delete=True)
        for i in a:
          await event.edit(i.original.action.message)
    else:
        await event.edit("`You need administrative permissions in order to do this command`")
        await asyncio.sleep(3)
        await event.delete()


async def get_user_from_event(event):
    if event.reply_to_msg_id:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
    else:
        user = event.pattern_match.group(1)
        if user.isnumeric():
            user = int(user)
        if not user:
            await event.edit("`Pass the user's username, id or reply!`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]

            if isinstance(probable_user_mention_entity, MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except (TypeError, ValueError) as err:
            await event.edit(str(err))
            return None
    return user_obj

async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await event.edit(str(err))
        return None
    return user_obj

