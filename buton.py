from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Məni Qrupa Əlavə Et", url=f"http://t.me/SozOyunTapmaBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🖥️ Məni Yaradan", url="t.me/Vusaliww"),
        InlineKeyboardButton("✅Rəsmi Kanal: ", url="https://t.me/cGuesMasterResmi"),
    ]
])



START ="""
 **Salam 👋\n\n**Mən @SozOyunTapmaBot Məni Qrupunuza Əlavə Edərək Söz Tapmaca Oynaya Bilərsiz\n\nƏminəmki Sizi Qoymayacam Sıxılmağa\n\n\nSizde Belə Bir Bot İstəyirsizsə : @Pyhchistion**
"""

    
    
    
    
    
    
"""
PRIVATE /start MESSAGE
"""
@Client.on_message(filters.command("start") & filters.private)
async def priv_start(c:Client, m:Message):
    await c.send_message(m.chat.id, START, reply_markup=keyboard)
