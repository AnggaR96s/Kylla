# Thanks to AvinashReddy for this Plugin

"""Download & Upload Images on Telegram
Syntax: `.img <Name>` or `.img (replied message)`
\n Upgraded by @NeoMatrix90 aka @kirito6969
"""


from google_images_download import google_images_download
import os
import shutil
from re import findall
from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern="img ?(.*)"))
async def img_sampler(event):
    await event.edit("`Processing Bsdk..`")
    reply = await event.get_reply_message()
    if event.pattern_match.group(1):
        query = event.pattern_match.group(1)
    elif reply:
        query = reply.message
    else:
        return
    
    lim = findall(r"lim=\d+", query)
    try:
        lim = lim[0]
        lim = lim.replace("lim=", "")
        query = query.replace("lim=" + lim[0], "")
    except IndexError:
        lim = 5
    response = google_images_download.googleimagesdownload()

    # creating list of arguments
    arguments = {
        "keywords": query,
        "limit": lim,
        "format": "jpg",
        "no_directory": "no_directory"
    }

    # passing the arguments to the function
    paths = response.download(arguments)
    lst = paths[0][query]
    await borg.send_file(await borg.get_input_entity(event.chat_id), lst)
    shutil.rmtree(os.path.dirname(os.path.abspath(lst[0])))
    await event.delete()
