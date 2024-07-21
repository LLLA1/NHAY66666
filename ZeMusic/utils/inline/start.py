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
            InlineKeyboardButton(text="𝐃𝐞𝐯", user_id=config.OWNER_ID),
            InlineKeyboardButton(text=config.CHANNEL_NAME, url=config.CHANNEL_LINK)
        ],
        [InlineKeyboardButton(text="𝐒𝐨𝐮𝐫𝐜𝐞 𝐥𝐨𝐥 🧚‍♀", url=f"https://t.me/K55DD"),
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
            InlineKeyboardButton(text="𝐃𝐞𝐯", user_id=config.OWNER_ID),
            InlineKeyboardButton(text=config.CHANNEL_NAME, url=config.CHANNEL_LINK)
        ],
        [InlineKeyboardButton(text="𝐒𝐨𝐮𝐫𝐜𝐞 𝐥𝐨𝐥 🧚‍♀", url=f"https://t.me/K55DD"),
 ],
    ]
    return buttons
