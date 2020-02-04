# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for kanging stickers or making new ones.
.kang
\nUsage: Reply .kang to a sticker or an image to kang it to your userbot pack.\
\n\n.kang [emoji('s)]
\nUsage: Works just like .kang but uses the emoji('s) you picked.\
\n\n.kang [number]
\nUsage: Kang's the sticker/image to the specified pack but uses 🔥 as emoji.\
\n\n.kang [emoji('s)] [number]
\nUsage: Kang's the sticker/image to the specified pack and uses the emoji('s) you picked.\
\n\n.packinfo
\nUsage: Gets info about the sticker pack.
\n\n.getsticker
\nUsage: Get compressed sticker pack."""

import io
import math
import urllib.request
from os import remove
from PIL import Image
import random
import os
import zipfile
import asyncio
import datetime
from collections import defaultdict
from telethon.tl.types import DocumentAttributeFilename, MessageMediaPhoto
from uniborg.util import admin_cmd
from sample_config import Config
from telethon.tl.functions.messages import GetStickerSetRequest
from telethon.tl.types import InputStickerSetID
from telethon.tl.types import DocumentAttributeSticker

KANGING_STR = [
    "Using Witchery to kang this sticker...",
    "Plagiarising hehe...",
    "Inviting this sticker over to my pack...",
    "Kanging this sticker...",
    "Hey that's a nice sticker!\nMind if I kang?!..",
    "hehe me stel ur stikér\nhehe.",
    "Ay look over there (☉｡☉)!→\nWhile I kang this...",
    "Roses are red violets are blue, kanging this sticker so my pacc looks cool",
    "Imprisoning this sticker...",
    "Mr.Steal Your Sticker is stealing this sticker... ",
]


@borg.on(admin_cmd(pattern="kang ?(.*)"))
async def kang(args):
    """ For .kang command, kangs stickers or creates new ones. """
    user = await borg.get_me()
    if not user.username:
        user.username = user.first_name
    message = await args.get_reply_message()
    photo = None
    emojibypass = False
    is_anim = False
    emoji = None

    if message and message.media:
        if isinstance(message.media, MessageMediaPhoto):
            await args.edit(f"`{random.choice(KANGING_STR)}`")
            photo = io.BytesIO()
            photo = await borg.download_media(message.photo, photo)
        elif "image" in message.media.document.mime_type.split('/'):
            await args.edit(f"`{random.choice(KANGING_STR)}`")
            photo = io.BytesIO()
            await borg.download_file(message.media.document, photo)
            if (DocumentAttributeFilename(file_name='sticker.webp') in
                    message.media.document.attributes):
                emoji = message.media.document.attributes[1].alt
                emojibypass = True
        elif "tgsticker" in message.media.document.mime_type:
            await args.edit(f"`{random.choice(KANGING_STR)}`")
            await borg.download_file(message.media.document,
                                    'AnimatedSticker.tgs')

            attributes = message.media.document.attributes
            for attribute in attributes:
                if isinstance(attribute, DocumentAttributeSticker):
                    emoji = attribute.alt

            emojibypass = True
            is_anim = True
            photo = 1
        else:
            await args.edit("`Unsupported File!`")
            return
    else:
        await args.edit("`I can't kang that...`")
        return

    if photo:
        splat = args.text.split()
        if not emojibypass:
            emoji = "🔥"
        pack = 1
        if len(splat) == 3:
            pack = splat[2]  # User sent both
            emoji = splat[1]
        elif len(splat) == 2:
            if splat[1].isnumeric():
                # User wants to push into different pack, but is okay with
                # thonk as emote.
                pack = int(splat[1])
            else:
                # User sent just custom emote, wants to push to default
                # pack
                emoji = splat[1]

        packname = f"a{user.id}_by_{user.username}_{pack}"
        packnick = f"@{user.username}'s kang pack Vol.{pack}"
        cmd = '/newpack'
        file = io.BytesIO()

        if not is_anim:
            image = await resize_photo(photo)
            file.name = "sticker.png"
            image.save(file, "PNG")
        else:
            packname += "_anim"
            packnick += " (Animated)"
            cmd = '/newanimated'

        response = urllib.request.urlopen(
            urllib.request.Request(f'http://t.me/addstickers/{packname}'))
        htmlstr = response.read().decode("utf8").split('\n')

        if "  A <strong>Telegram</strong> user has created the <strong>Sticker&nbsp;Set</strong>." not in htmlstr:
            async with borg.conversation('Stickers') as conv:
                await conv.send_message('/addsticker')
                await conv.get_response()
                # Ensure user doesn't get spamming notifications
                await borg.send_read_acknowledge(conv.chat_id)
                await conv.send_message(packname)
                x = await conv.get_response()
                while "120" in x.text:
                    pack += 1
                    packname = f"a{user.id}_by_{user.username}_{pack}"
                    packnick = f"@{user.username}'s kang pack Vol.{pack}"
                    await args.edit("`Switching to Pack " + str(pack) +
                                    " due to insufficient space`")
                    await conv.send_message(packname)
                    x = await conv.get_response()
                    if x.text == "Invalid pack selected.":
                        await conv.send_message(cmd)
                        await conv.get_response()
                        # Ensure user doesn't get spamming notifications
                        await borg.send_read_acknowledge(conv.chat_id)
                        await conv.send_message(packnick)
                        await conv.get_response()
                        # Ensure user doesn't get spamming notifications
                        await borg.send_read_acknowledge(conv.chat_id)
                        if is_anim:
                            await conv.send_file('AnimatedSticker.tgs')
                            remove('AnimatedSticker.tgs')
                        else:
                            file.seek(0)
                            await conv.send_file(file, force_document=True)
                        await conv.get_response()
                        await conv.send_message(emoji)
                        # Ensure user doesn't get spamming notifications
                        await borg.send_read_acknowledge(conv.chat_id)
                        await conv.get_response()
                        await conv.send_message("/publish")
                        if is_anim:
                            await conv.get_response()
                            await conv.send_message(f"<{packnick}>")
                        # Ensure user doesn't get spamming notifications
                        await conv.get_response()
                        await borg.send_read_acknowledge(conv.chat_id)
                        await conv.send_message("/skip")
                        # Ensure user doesn't get spamming notifications
                        await borg.send_read_acknowledge(conv.chat_id)
                        await conv.get_response()
                        await conv.send_message(packname)
                        # Ensure user doesn't get spamming notifications
                        await borg.send_read_acknowledge(conv.chat_id)
                        await conv.get_response()
                        # Ensure user doesn't get spamming notifications
                        await borg.send_read_acknowledge(conv.chat_id)
                        await args.edit(f"`Sticker added in a Different Pack !\
                            \nThis Pack is Newly created!\
                            \nYour pack can be found [here](t.me/addstickers/{packname})",
                                        parse_mode='md')
                        return
                if is_anim:
                    await conv.send_file('AnimatedSticker.tgs')
                    remove('AnimatedSticker.tgs')
                else:
                    file.seek(0)
                    await conv.send_file(file, force_document=True)
                rsp = await conv.get_response()
                if "Sorry, the file type is invalid." in rsp.text:
                    await args.edit(
                        "`Failed to add sticker, use` @Stickers `bot to add the sticker manually.`"
                    )
                    return
                await conv.send_message(emoji)
                # Ensure user doesn't get spamming notifications
                await borg.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await conv.send_message('/done')
                await conv.get_response()
                # Ensure user doesn't get spamming notifications
                await borg.send_read_acknowledge(conv.chat_id)
        else:
            await args.edit("`Brewing a new Pack...`")
            async with borg.conversation('Stickers') as conv:
                await conv.send_message(cmd)
                await conv.get_response()
                # Ensure user doesn't get spamming notifications
                await borg.send_read_acknowledge(conv.chat_id)
                await conv.send_message(packnick)
                await conv.get_response()
                # Ensure user doesn't get spamming notifications
                await borg.send_read_acknowledge(conv.chat_id)
                if is_anim:
                    await conv.send_file('AnimatedSticker.tgs')
                    remove('AnimatedSticker.tgs')
                else:
                    file.seek(0)
                    await conv.send_file(file, force_document=True)
                rsp = await conv.get_response()
                if "Sorry, the file type is invalid." in rsp.text:
                    await args.edit(
                        "`Failed to add sticker, use` @Stickers `bot to add the sticker manually.`"
                    )
                    return
                await conv.send_message(emoji)
                # Ensure user doesn't get spamming notifications
                await borg.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await conv.send_message("/publish")
                if is_anim:
                    await conv.get_response()
                    await conv.send_message(f"<{packnick}>")
                # Ensure user doesn't get spamming notifications
                await conv.get_response()
                await borg.send_read_acknowledge(conv.chat_id)
                await conv.send_message("/skip")
                # Ensure user doesn't get spamming notifications
                await borg.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                await conv.send_message(packname)
                # Ensure user doesn't get spamming notifications
                await borg.send_read_acknowledge(conv.chat_id)
                await conv.get_response()
                # Ensure user doesn't get spamming notifications
                await borg.send_read_acknowledge(conv.chat_id)

        await args.edit(f"`Sticker kanged successfully!`\
            \nPack can be found [here](t.me/addstickers/{packname})",
                        parse_mode='md')


async def resize_photo(photo):
    """ Resize the given photo to 512x512 """
    image = Image.open(photo)
    maxsize = (512, 512)
    if (image.width and image.height) < 512:
        size1 = image.width
        size2 = image.height
        if image.width > image.height:
            scale = 512 / size1
            size1new = 512
            size2new = size2 * scale
        else:
            scale = 512 / size2
            size1new = size1 * scale
            size2new = 512
        size1new = math.floor(size1new)
        size2new = math.floor(size2new)
        sizenew = (size1new, size2new)
        image = image.resize(sizenew)
    else:
        image.thumbnail(maxsize)

    return image


@borg.on(admin_cmd(pattern="packinfo ?(.*)"))
async def get_pack_info(event):
    if not event.is_reply:
        await event.edit("`I can't fetch info from nothing, can I ?!`")
        return

    rep_msg = await event.get_reply_message()
    if not rep_msg.document:
        await event.edit("`Reply to a sticker to get the pack details`")
        return

    try:
        stickerset_attr = rep_msg.document.attributes[1]
        await event.edit(
            "`Fetching details of the sticker pack, please wait..`")
    except BaseException:
        await event.edit("`This is not a sticker. Reply to a sticker.`")
        return

    if not isinstance(stickerset_attr, DocumentAttributeSticker):
        await event.edit("`This is not a sticker. Reply to a sticker.`")
        return

    get_stickerset = await borg(
        GetStickerSetRequest(
            InputStickerSetID(
                id=stickerset_attr.stickerset.id,
                access_hash=stickerset_attr.stickerset.access_hash)))
    pack_emojis = []
    for document_sticker in get_stickerset.packs:
        if document_sticker.emoticon not in pack_emojis:
            pack_emojis.append(document_sticker.emoticon)

    OUTPUT = f"**Sticker Title:** `{get_stickerset.set.title}\n`" \
        f"**Sticker Short Name:** `{get_stickerset.set.short_name}`\n" \
        f"**Official:** `{get_stickerset.set.official}`\n" \
        f"**Archived:** `{get_stickerset.set.archived}`\n" \
        f"**Stickers In Pack:** `{len(get_stickerset.packs)}`\n" \
        f"**Emojis In Pack:**\n{' '.join(pack_emojis)}"

    await event.edit(OUTPUT)

@borg.on(admin_cmd(pattern="getsticker ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        # https://gist.github.com/udf/e4e3dbb2e831c8b580d8fddd312714f7
        if not reply_message.sticker:
            return
        sticker = reply_message.sticker
        sticker_attrib = find_instance(sticker.attributes, DocumentAttributeSticker)
        if not sticker_attrib.stickerset:
            await event.reply("This sticker is not part of a pack")
            return
        is_a_s = is_it_animated_sticker(reply_message)
        file_ext_ns_ion = "webp"
        # file_caption = "https://t.me/RoseSupport/33801"
        if is_a_s:
            file_ext_ns_ion = "tgs"
            file_caption = "Forward the ZIP file to @AnimatedStickersRoBot to get lottIE JSON containing the vector information."
        sticker_set = await borg(GetStickerSetRequest(sticker_attrib.stickerset))
        pack_file = os.path.join(Config.TMP_DOWNLOAD_DIRECTORY, sticker_set.set.short_name, "pack.txt")
        if os.path.isfile(pack_file):
            os.remove(pack_file)
        # Sticker emojis are retrieved as a mapping of
        # <emoji>: <list of document ids that have this emoji>
        # So we need to build a mapping of <document id>: <list of emoji>
        # Thanks, Durov
        emojis = defaultdict(str)
        for pack in sticker_set.packs:
            for document_id in pack.documents:
                emojis[document_id] += pack.emoticon
        async def download(sticker, emojis, path, file):
            await borg.download_media(sticker, file=os.path.join(path, file))
            with open(pack_file, "a") as f:
                f.write(f"{{'image_file': '{file}','emojis':{emojis[sticker.id]}}},")
        pending_tasks = [
            asyncio.ensure_future(
                download(document, emojis, Config.TMP_DOWNLOAD_DIRECTORY + sticker_set.set.short_name, f"{i:03d}.{file_ext_ns_ion}")
            ) for i, document in enumerate(sticker_set.documents)
        ]
        await event.edit(f"Downloading {sticker_set.set.count} sticker(s) to .{Config.TMP_DOWNLOAD_DIRECTORY}{sticker_set.set.short_name}...")
        num_tasks = len(pending_tasks)
        while 1:
            done, pending_tasks = await asyncio.wait(pending_tasks, timeout=2.5,
                return_when=asyncio.FIRST_COMPLETED)
            try:
                await event.edit(
                    f"Downloaded {num_tasks - len(pending_tasks)}/{sticker_set.set.count}")
            except MessageNotModifiedError:
                pass
            if not pending_tasks:
                break
        await event.edit("Downloading to my local completed")
        # https://gist.github.com/udf/e4e3dbb2e831c8b580d8fddd312714f7
        directory_name = Config.TMP_DOWNLOAD_DIRECTORY + sticker_set.set.short_name
        zipf = zipfile.ZipFile(directory_name + ".zip", "w", zipfile.ZIP_DEFLATED)
        zipdir(directory_name, zipf)
        zipf.close()
        await borg.send_file(
            event.chat_id,
            directory_name + ".zip",
            force_document=True,
            allow_cache=False,
            reply_to=event.message.id,
            progress_callback=progress
        )
        try:
            os.remove(directory_name + ".zip")
            os.remove(directory_name)
        except:
            pass
        await event.edit("task Completed")
        await asyncio.sleep(3)
        await event.delete()
    else:
        await event.edit("TODO: Not Implemented")

# helper

def is_it_animated_sticker(message):
    try:
        if message.media and message.media.document:
            mime_type = message.media.document.mime_type
            if "tgsticker" in mime_type:
                return True
            else:
                return False
        else:
            return False
    except:
        return False

def progress(current, total):
    logger.info("Uploaded: {} of {}\nCompleted {}".format(current, total, (current / total) * 100))


def find_instance(items, class_or_tuple):
    for item in items:
        if isinstance(item, class_or_tuple):
            return item
    return None


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            os.remove(os.path.join(root, file))
