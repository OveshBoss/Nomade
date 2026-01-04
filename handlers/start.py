# ============================================================
# Group Manager Bot
# Author: LearningBotsOfficial (https://github.com/LearningBotsOfficial) 
# Support: https://t.me/LearningBotsCommunity
# Channel: https://t.me/learning_bots
# YouTube: https://youtube.com/@learning_bots
# License: Open-source (keep credits, no resale)
# ============================================================

from pyrogram import Client, filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto
)
from config import BOT_USERNAME, SUPPORT_GROUP, UPDATE_CHANNEL, START_IMAGE, OWNER_ID
import db

def register_handlers(app: Client):

# ==========================================================
# Start Message (Small Caps & New Design)
# ==========================================================
    async def send_start_menu(message, user):
        text = f"""
✨ **ʜᴇʟʟᴏ {user}!** ✨

👋 **ɪ ᴀᴍ ʙᴏss ᴍᴀɴᴀɢᴇʀ 🤖** **ʜɪɢʜʟɪɢʜᴛs:**
─────────────────────────────
- 🛡️ **sᴍᴀʀᴛ ᴀɴᴛɪ-sᴘᴀᴍ & ʟɪɴᴋ sʜɪᴇʟᴅ**
- 🔐 **ᴀᴅᴀᴘᴛɪᴠᴇ ʟᴏᴄᴋ sʏsᴛᴇᴍ (ᴜʀʟs, ᴍᴇᴅɪᴀ)**
- 🧩 **ᴍᴏᴅᴜʟᴀʀ & sᴄᴀʟᴀʙʟᴇ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ**
- 🎨 **sʟᴇᴇᴋ ᴜɪ ᴡɪᴛʜ ɪɴʟɪɴᴇ ᴄᴏɴᴛʀᴏʟs**

» **ᴍᴏʀᴇ ɴᴇᴡ ꜰᴇᴀᴛᴜʀᴇs ᴄᴏᴍɪɴɢ sᴏᴏɴ ...**
"""

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("⚒️ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⚒️", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [
                InlineKeyboardButton("🏠 sᴜᴘᴘᴏʀᴛ", url=SUPPORT_GROUP),
                InlineKeyboardButton("📢 ᴜᴘᴅᴀᴛᴇs", url=UPDATE_CHANNEL),
            ],
            [
                InlineKeyboardButton("👤 ᴏᴡɴᴇʀ", url=f"tg://user?id={OWNER_ID}"),
                InlineKeyboardButton("ఌ︎ ʀᴇᴘᴏ ఌ︎", url="https://github.com/OveshBoss/Nomade"),
            ],
            [InlineKeyboardButton("📚 ʜᴇʟᴘ ᴄᴏᴍᴍᴀɴᴅs 📚", callback_data="help")]
        ])

        if message.text:
            await message.reply_photo(START_IMAGE, caption=text, reply_markup=buttons)
        else:
            media = InputMediaPhoto(media=START_IMAGE, caption=text)
            await message.edit_media(media=media, reply_markup=buttons)

# ==========================================================
# Start Command (With Emoji Reaction)
# ==========================================================
    @app.on_message(filters.private & filters.command("start"))
    async def start_command(client, message):
        user = message.from_user
        
        # Adding Emoji Reaction (⚡)
        try:
            await message.react("⚡")
        except:
            pass
            
        await db.add_user(user.id, user.first_name)
        await send_start_menu(message, user.first_name)

# ==========================================================
# Help Menu Message (Small Caps)
# ==========================================================
    async def send_help_menu(message):
        text = """
╔══════════════════╗
     **ʜᴇʟᴘ ᴍᴇɴᴜ**
╚══════════════════╝

**ᴄʜᴏᴏsᴇ ᴀ ᴄᴀᴛᴇɢᴏʀʏ ʙᴇʟᴏᴡ:**
─────────────────────────────
"""
        buttons = InlineKeyboardMarkup([
            [
                InlineKeyboardButton("👋 ɢʀᴇᴇᴛɪɴɢs", callback_data="greetings"),
                InlineKeyboardButton("🔒 ʟᴏᴄᴋs", callback_data="locks"),
            ],
            [
                InlineKeyboardButton("🛡️ ᴍᴏᴅᴇʀᴀᴛɪᴏɴ", callback_data="moderation")
            ],
            [InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="back_to_start")]
        ])

        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await message.edit_media(media=media, reply_markup=buttons)

# ==========================================================
# All Callbacks (Updated with Small Caps)
# ==========================================================
    @app.on_callback_query(filters.regex("help"))
    async def help_callback(client, callback_query):
        await send_help_menu(callback_query.message)
        await callback_query.answer()

    @app.on_callback_query(filters.regex("back_to_start"))
    async def back_to_start_callback(client, callback_query):
        user = callback_query.from_user.first_name
        await send_start_menu(callback_query.message, user)
        await callback_query.answer()

    @app.on_callback_query(filters.regex("greetings"))
    async def greetings_callback(client, callback_query):
        text = """
╔══════════════════╗
    **ᴡᴇʟᴄᴏᴍᴇ sʏsᴛᴇᴍ**
╚══════════════════╝

**ᴄᴏᴍᴍᴀɴᴅs:**
- `/setwelcome <text>` : **sᴇᴛ ᴄᴜsᴛᴏᴍ ᴍsɢ**
- `/welcome on` : **ᴇɴᴀʙʟᴇ**
- `/welcome off` : **ᴅɪsᴀʙʟᴇ**

**ᴘʟᴀᴄᴇʜᴏʟᴅᴇʀs:**
`{username}`, `{first_name}`, `{id}`, `{mention}`
"""
        buttons = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")]])
        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await callback_query.message.edit_media(media=media, reply_markup=buttons)
        await callback_query.answer()

    @app.on_callback_query(filters.regex("locks"))
    async def locks_callback(client, callback_query):
        text = """
╔══════════════════╗
     **ʟᴏᴄᴋs sʏsᴛᴇᴍ**
╚══════════════════╝

**ᴄᴏᴍᴍᴀɴᴅs:**
- `/lock <type>` : **ᴇɴᴀʙʟᴇ ʟᴏᴄᴋ**
- `/unlock <type>` : **ᴅɪsᴀʙʟᴇ ʟᴏᴄᴋ**

**ᴛʏᴘᴇs:**
`url`, `sticker`, `media`, `username`, `language`
"""
        buttons = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")]])
        media = InputMediaPhoto(media=START_IMAGE, caption=text)
        await callback_query.message.edit_media(media=media, reply_markup=buttons)
        await callback_query.answer()

    @app.on_callback_query(filters.regex("moderation"))
    async def info_callback(client, callback_query):
        try:
            text = """
╔══════════════════╗
      **ᴍᴏᴅᴇʀᴀᴛɪᴏɴ**
╚══════════════════╝

**ᴀᴠᴀɪʟᴀʙʟᴇ ᴛᴏᴏʟs:**
¤ `/kick` — **ʀᴇᴍᴏᴠᴇ ᴜsᴇʀ**
¤ `/ban` — **ʙᴀɴ ᴜsᴇʀ**
¤ `/mute` — **sɪʟᴇɴᴄᴇ ᴜsᴇʀ**
¤ `/warn` — **ɢɪᴠᴇ ᴡᴀʀɴɪɴɢ**
¤ `/promote` — **ᴀᴅᴅ ᴀᴅᴍɪɴ**
¤ `/demote` — **ʀᴇᴍᴏᴠᴇ ᴀᴅᴍɪɴ**
"""
            buttons = InlineKeyboardMarkup([[InlineKeyboardButton("🔙 ʙᴀᴄᴋ", callback_data="help")]])
            media = InputMediaPhoto(media=START_IMAGE, caption=text)
            await callback_query.message.edit_media(media=media, reply_markup=buttons)
            await callback_query.answer()
        except Exception as e:
            await callback_query.answer("❌ **ᴇʀʀᴏʀ!**", show_alert=True)

# ==========================================================
# Broadcast & Stats
# ==========================================================
    @app.on_message(filters.private & filters.command("broadcast"))
    async def broadcast_message(client, message):
        if message.from_user.id != OWNER_ID:
            return await message.reply_text("❌ **ᴏɴʟʏ ᴏᴡɴᴇʀ ᴄᴀɴ ᴜsᴇ ᴛʜɪs!**")
        
        if not message.reply_to_message:
            return await message.reply_text("⚠️ **ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍsɢ!**")

        users = await db.get_all_users()
        sent = 0
        for user_id in users:
            try:
                await message.reply_to_message.copy(user_id)
                sent += 1
            except: pass
        await message.reply_text(f"✅ **ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏɴᴇ! sᴇɴᴛ ᴛᴏ {sent} ᴜsᴇʀs.**")

    @app.on_message(filters.private & filters.command("stats"))
    async def stats_command(client, message):
        if message.from_user.id != OWNER_ID:
            return
        users = await db.get_all_users()
        await message.reply_text(f"📊 **ᴛᴏᴛᴀʟ ᴜsᴇʀs:** `{len(users)}`")
