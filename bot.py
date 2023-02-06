from pyrogram import Client, filters
from pyrogram.types import Message

from config import log
import config

app = Client(**log, )


@app.on_message(filters.chat(int(config.bot_id)))
async def resend_text(client: Client, message: Message):
    mess = message.text
    await app.send_message(int(config.channel), mess)


if __name__ == '__main__':
    app.run()