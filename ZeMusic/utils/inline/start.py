from pyrogram.types import InlineKeyboardButton
import config
from ZeMusic import app

Lnk= "https://t.me/" +config.CHANNEL_LINK

def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="أضفني إلى مجموعتك او قناتك",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الأوامر", callback_data="zzzback")],
        [
            InlineKeyboardButton(text="السورس", url=config.CHANNEL_LINK),
            InlineKeyboardButton(text="المتجر", url=f"https://t.me/YMMYN")
        ],
        [InlineKeyboardButton(text="𝐃𝐞𝐯 𝐖𝐨𝐫𝐝", url=f"https://t.me/KHAYAL70"),
],

    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="أضفني إلى مجموعتك او قناتك",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="الأوامر", callback_data="zzzback")],
        [
            InlineKeyboardButton(text="السورس", url=config.CHANNEL_LINK),
            InlineKeyboardButton(text="المتجر", url=f"https://t.me/YMMYN")
        ],
        [InlineKeyboardButton(text="𝐃𝐞𝐯 𝐖𝐨𝐫𝐝", url=f"https://t.me/KHAYAL70"),
 ],
    ]
    return buttons
