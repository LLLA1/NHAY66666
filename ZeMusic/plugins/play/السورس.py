import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/d030044dbdc7c4133b0c5.jpg",
        caption = f"""<b>  <b>\n<a href="https://t.me/K55DD"> ➮ 𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐒𝐨𝐮𝐫𝐜𝐞 𝐥𝐨𝐥 🧚‍♀</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                         "𝐃𝐞𝐯 𝐒𝐨𝐮𝐫𝐜𝐞", url=f"https://t.me/F_A_6"), 
                 ],[
                   InlineKeyboardButton(
                        "𝐒𝐨𝐮𝐫𝐜𝐞 𝐥𝐨𝐥 🧚‍♀", url=f"https://t.me/K55DD"),
                ],

            ]

        ),

    )
