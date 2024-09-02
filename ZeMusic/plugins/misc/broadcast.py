import asyncio

# مكتبة Pyrogram للتفاعل مع Telegram API
from pyrogram import filters
from pyrogram.enums import ChatMembersFilter
from pyrogram.errors import FloodWait

# استيراد التطبيق والمكونات المختلفة من مشروع ZeMusic
from ZeMusic import app  # تطبيق البوت
from ZeMusic.misc import SUDOERS  # قائمة بالمستخدمين الـ SUDOERS

# دوال التعامل مع قاعدة البيانات
from ZeMusic.utils.database import (
    get_active_chats,     # دالة للحصول على دردشات نشطة
    get_authuser_names,   # دالة للحصول على أسماء المستخدمين المعتمدين
    get_client,           # دالة للحصول على عميل معين
    get_served_chats,     # دالة للحصول على دردشات البوت
    get_served_users,     # دالة للحصول على مستخدمي البوت
)

# إضافات اللغة والتنسيق
from ZeMusic.utils.decorators.language import language  # دالة معالجة اللغة
from ZeMusic.utils.formatters import alpha_to_int  # دالة تحويل الألفا إلى عدد صحيح

# إعدادات التكوين
from config import adminlist, OWNER_ID  # إعدادات المسؤولين ومعرف المالك
IS_BROADCASTING = False

@app.on_message(filters.command(["broadcast", "اذاعه"]) & SUDOERS)
@language
async def broadcast_message(client, message, _):
    global IS_BROADCASTING
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("لا تملك صلاحيات البث.")
    
    await message.reply_text("اختر نوع البث:\n1. بث إلى جميع دردشات البوت\n2. بث إلى محادثات المستخدمين الخاصين")

    # انتظار رد من OWNER_ID لاختيار النوع
        # تأكد من استخدام دالة صحيحة لاستقبال الرسائل، استبدل 'wait_for_message' بالدالة الصحيحة إذا كانت مختلفة
response = await client.wait_for_message(message.chat.id)  # إضافة لتلقي رد المستخدم

if response and response.text == "1":  # تحقق من ما إذا كانت الاستجابة صحيحة
    await broadcast_to_chats(message)  # تأكد من تمرير الرسالة الصحيحة
elif response and response.text == "2":
    await broadcast_to_users(message)  # تأكد من تمرير الرسالة الصحيحة
else:
    await client.send_message(message.chat.id, "اختيار غير صحيح. البث ملغى.")
        
async def broadcast_to_chats(message, _):
    global IS_BROADCASTING
    IS_BROADCASTING = True
    
    if message.reply_to_message:
        query = message.reply_to_message.text  # أخذ الرسالة من الرد
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_2"])
        query = message.text.split(None, 1)[1].strip()
        if query == "":
            return await message.reply_text(_["broad_8"])

    await message.reply_text(_["broad_1"])
    
    sent = 0
    chats = await get_served_chats()
    
    for chat in chats:
        try:
            await app.send_message(chat["chat_id"], text=query)
            sent += 1
            await asyncio.sleep(0.2)
        except FloodWait as fw:
            await asyncio.sleep(int(fw.value))
        except Exception as e:
            print(f"خطأ في إرسال الرسالة إلى الدردشة {chat['chat_id']}: {e}")
            continue

    await message.reply_text(_["broad_3"].format(sent))  # عدد الرسائل المرسلة
    IS_BROADCASTING = False

async def broadcast_to_users(message, _):
    global IS_BROADCASTING
    IS_BROADCASTING = True
    
    if message.reply_to_message:
        query = message.reply_to_message.text  # أخذ الرسالة من الرد
    else:
        if len(message.command) < 2:
            return await message.reply_text(_["broad_2"])
        query = message.text.split(None, 1)[1].strip()
        if query == "":
            return await message.reply_text(_["broad_8"])

    await message.reply_text(_["broad_1"])
    
    susr = 0
    users = await get_served_users()
    
    for user in users:
        try:
            await app.send_message(user["user_id"], text=query)
            susr += 1
            await asyncio.sleep(0.2)
        except FloodWait as fw:
            await asyncio.sleep(int(fw.value))
        except Exception as e:
            print(f"خطأ في إرسال الرسالة إلى المستخدم {user['user_id']}: {e}")
            continue
    
    await message.reply_text(_["broad_4"].format(susr))
    IS_BROADCASTING = False

async def auto_clean():
    while True:
        await asyncio.sleep(10)
        try:
            served_chats = await get_active_chats()
            for chat_id in served_chats:
                if chat_id not in adminlist:
                    adminlist[chat_id] = []
                    async for user in app.get_chat_members(chat_id, filter=ChatMembersFilter.ADMINISTRATORS
                    ):
                        if user.privileges.can_manage_video_chats:
                            adminlist[chat_id].append(user.user.id)
                    authusers = await get_authuser_names(chat_id)
                    for user in authusers:
                        user_id = await alpha_to_int(user)
                        adminlist[chat_id].append(user_id)
        except Exception as e:
            print(f"خطأ في تحديث المسؤولين: {e}")
            continue

# بدء مهمة التنظيف في الخلفية
asyncio.create_task(auto_clean())
