
# For UniBorg
# Copyright (c) JeepBot | 2019 
# (c) JeepBot is not occur to all modules in here
"""
Imdb Module
.imdb
"""

import bs4
import requests
import asyncio
import os
import re
import subprocess
import time
from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd

langi = "en"

#kanged from Blank-x ;---;
@borg.on(admin_cmd(pattern="imdb ?(.*)")) 
async def imdb(e):
 sticktext = e.pattern_match.group(1)
 
 if not sticktext:
    	get = await e.get_reply_message()
    	sticktext = get.text

 try:
    movie_name = sticktext
    remove_space = movie_name.split(' ')
    final_name = '+'.join(remove_space)
    page = requests.get("https://www.imdb.com/find?ref_=nv_sr_fn&q="+final_name+"&s=all")
    lnk = str(page.status_code)
    soup = bs4.BeautifulSoup(page.content,'lxml')
    odds = soup.findAll("tr","odd")
    mov_title = odds[0].findNext('td').findNext('td').text
    mov_link = "http://www.imdb.com/"+odds[0].findNext('td').findNext('td').a['href']
    page1 = requests.get(mov_link)
    soup = bs4.BeautifulSoup(page1.content,'lxml')
    if soup.find('div','poster'):
    	poster = soup.find('div','poster').img['src']

    else:
    	poster = ''
    if soup.find('div','title_wrapper'):
    	pg = soup.find('div','title_wrapper').findNext('div').text
    	mov_details = re.sub(r'\s+',' ',pg)
    else:
    	mov_details = ''
    credits = soup.findAll('div', 'credit_summary_item')
    if len(credits)==1:
    	director = credits[0].a.text
    	writer = 'Not available'
    	stars = 'Not available'
    elif len(credits)>2:
    	director = credits[0].a.text
    	writer = credits[1].a.text
    	actors = []
    	for x in credits[2].findAll('a'):
    		actors.append(x.text)
    	actors.pop()
    	stars = actors[0]+','+actors[1]+','+actors[2]
    else:
    	director = credits[0].a.text
    	writer = 'Not available'
    	actors = []
    	for x in credits[1].findAll('a'):
    		actors.append(x.text)
    	actors.pop()
    	stars = actors[0]+','+actors[1]+','+actors[2]
    if soup.find('div', "inline canwrap"):
    	story_line = soup.find('div', "inline canwrap").findAll('p')[0].text
    else:
    	story_line = 'Not available'
    info = soup.findAll('div', "txt-block")
    if info:
    	mov_country = []
    	mov_language = []
    	for node in info:
    		a = node.findAll('a')
    		for i in a:
    			if "country_of_origin" in i['href']:
    				mov_country.append(i.text)
    			elif "primary_language" in i['href']:
    				mov_language.append(i.text)
    if soup.findAll('div',"ratingValue"):
    	for r in soup.findAll('div',"ratingValue"):
    		mov_rating = r.strong['title']
    else:
    	mov_rating = 'Not available'
    await e.edit('<a href='+poster+'>&#8203;</a>'
    			'<b>Title : </b><code>'+mov_title+
    			'</code>\n<b>Details : </b><code>'+mov_details+
    			'</code>\n<b>Rating : </b><code>'+mov_rating+
    			'</code>\n<b>Country : </b><code>'+mov_country[0]+
    			'</code>\n<b>Language : </b><code>'+mov_language[0]+
    			'</code>\n<b>Director : </b><code>'+director+
    			'</code>\n<b>Writer : </b><code>'+writer+
    			'</code>\n<b>Stars : </b><code>'+stars+
    			'</code>\n<b>IMDB Url : </b>'+mov_link+
    			'\n<b>Story Line : </b>'+story_line,
    			link_preview = True , parse_mode = 'HTML'
    			)
 except IndexError:
     await e.edit("Plox enter **Valid movie name** kthx")

@borg.on(admin_cmd(pattern="film ?(.*)"))
async def let_me_google_that_for_youu(lmgtfyy_q):
    textx = await lmgtfyy_q.get_reply_message()
    qry = lmgtfyy_q.pattern_match.group(1)
    if qry:
        query = str(qry)
    elif textx:
        query = textx
        query = query.message
    query_encoded = query.replace(" ", "+")
    lfy_url = f"http://dunia21.org/?s={query_encoded}"
    payload = {'format': 'json', 'url': lfy_url}
    r = requests.get('http://is.gd/create.php', params=payload)
    await lmgtfyy_q.edit(f"Link for movie [{query}]({r.json()['shorturl']})")
