'''

    telegram bot
    YoungKwangKim9728_Bot
'''

import telepot

f = open("idKey", 'r')
id = f.readline()
token = "850452568:AAHw3xxLmmZX8kkxwIt0LcutMVud_9pzAqg"
print(id)
print(token)

bot = telepot.Bot(token)

# text message
# bot.sendMessage(id,"test message")

# image
bot.sendChatAction(id, "upload_photo")
bot.sendPhoto(id, open('test.jpg', 'rb'), caption="test image")




