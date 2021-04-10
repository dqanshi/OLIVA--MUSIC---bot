from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 🎵

I can play music in your group's voice call. Developed by [Hackelite](https://t.me/hackelite01).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://t.me/mayank_ka_b_for_bot")
                  ],[
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/hackelite02"
                    ),
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/hackelitebotlist"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➄1�7 Add To Your Group ➄1�7", url="https://t.me/TG_Group_Music_VC_V2_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online ✄1�7**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🔊 Channel", url="https://t.me/hackelitebotlist")
                ]
            ]
        )
   )


