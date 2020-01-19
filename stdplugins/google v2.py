import datetime
import asyncio
import shutil
from bs4 import BeautifulSoup
import re
from html import unescape
from re import findall
from selenium import webdriver
from urllib.parse import quote_plus
from urllib.error import HTTPError
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
from requests import get
from search_engine_parser import GoogleSearch
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import asyncio
from telethon import events
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="google ?(.*)"))
async def gsearch(q_event):
    """ For .google command, do a Google search. """
    await q_event.edit("""`Ruk Bsdk tera IP Ban karwata Hoon`""")
    reply = await q_event.get_reply_message()
    if q_event.pattern_match.group(1):
        url = q_event.pattern_match.group(1)
    elif reply is not None:
        url = reply.message
    else:
        return
    page = findall(r"page=\d+", url)
    try:
        page = page[0]
        page = page.replace("page=", "")
        url = url.replace("page=" + page[0], "")
    except IndexError:
        page = 1
    search_args = (str(url), int(page))
    gsearch = GoogleSearch()
    gresults = await gsearch.async_search(*search_args)
    msg = ""
    i = 1
    
    for i in range(11):
        try:
            title = gresults["titles"][i]
            link = gresults["links"][i]
            desc = gresults["descriptions"][i]
            msg += f"{i}. [{title}]({link})\n`{desc}`\n\n"
        except IndexError:
            break
            
            i += 1

    await q_event.edit("**Search Query:**\n`" + url + "`\n\n**Results:**\n" +
                       msg,
                       link_preview=False)
