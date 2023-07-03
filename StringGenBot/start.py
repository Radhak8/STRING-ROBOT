from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""𝐇𝐞𝐲 {msg.from_user.mention}🍷,

𝐈 𝐀𝐦 {me2},
𝐓𝐑𝐔𝐒𝐓𝐄𝐃 𝐒𝐓𝐑𝐈𝐍𝐆 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐎𝐑 𝐁𝐎𝐓.
𝐅𝐔𝐋𝐋𝐘 𝐒𝐀𝐅𝐄 & 𝐒𝐄𝐂𝐔𝐑𝐄.
𝐍𝐎 𝐀𝐌𝐘 𝐄𝐑𝐑𝐎𝐑.

𝐌𝐚𝐝𝐞 𝐁𝐲  : [Rᴀᴅʜᴀ Sɪɴɢʜ](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⚡𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐓𝐑𝐈𝐍𝐆⚡", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("❣️ Sᴜᴘᴘᴏʀᴛ ❣️", url="https://t.me/RadhaX2Support"),
                    InlineKeyboardButton("🥀 Oғғɪᴄᴇ 🥀", url="https://t.me/RadhaX2Update")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
