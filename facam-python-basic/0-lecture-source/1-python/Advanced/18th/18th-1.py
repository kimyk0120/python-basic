import telepot

bot = telepot.Bot('661295548:AAFJ6__a7HvM3qchm76BlA5lfavPW1pSkV8')
# bot.sendMessage('57841042', '안녕하세요')

bot.sendChatAction('57841042', 'upload_document')
bot.sendPhoto('57841042', open('profile.png', 'rb'), caption='프로필사진')
