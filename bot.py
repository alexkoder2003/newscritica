from pyrogram import Client, Filters, InlineKeyboardMarkup, InlineKeyboardButton
import custom_utils
import os
from decouple import config


app2 = Client(
    'criticalsite_bot',
    api_id= '1252175' ,
    api_hash= '46648b03fb24eaa7ce7f1ab1fdc6d7f5' ,
    bot_token= '999129543:AAE-Vq0DihmvIFanHi7-757tH5Rg-acIwS0' ,
)


@app2.on_message(Filters.regex('http'))
def post(client, message):
    if message.chat.username == 'screlizer' or 'Alex_Xakep':
        url = message.text
        text = custom_utils.parsing(url)
        client.send_message(
            'newscritica',
            text[0],
            reply_markup=InlineKeyboardMarkup([[
                InlineKeyboardButton('Читать новость!', url=text[1]),
            ]]),
        )

app2.run()

