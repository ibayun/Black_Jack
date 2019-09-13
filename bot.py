import telebot
import requests

TOKEN = "925351426:AAHzTYMJXTZOxlqlohzdF-IEJKpUKyfOIuk"


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['text'])
def start_message(message):
     bot.send_message(
        message.chat.id,
         "Привет! Я бот игры в black jack. Нажми {start_games} "
         "- чтобы начать игру, {rules} - чтобы узнать правила игры"
    )


@bot.message_handler(content_types=["start_games"])
def handle_answer(message):
    print(dir(message.text))
    bot.send_message(
        message.chat.id, "должна начаться игра"
    )

@bot.message_handler(content_types=["rules"])
def handle_answer(message):
    print(dir(message.text))
    bot.send_message(
        message.chat.id, "правила:"
    )


"""@bot.message_handler(content_types=["text"])
def handle_answer(message):
    print(dir(message.text))
    bot.send_message(
        message.chat.id, message.text
    )
"""

    """
    if message.text == "Привет":
    bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
    bot.send_message(message.from_user.id, "Напиши привет")else:
    bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")"""


if __name__ == "__main__":
    bot.polling(none_stop=True)
"""@bot.message_handler(commands=['help'])
def help_command(message):
    keyboard = telebot.types.InlineKeyboardMarkup()
    keyboard.add( telebot.types.InlineKeyboardButton( 'Message the developer', url='telegram.me/artiomtb' ) )
    bot.send_message( message.chat.id, '1) To receive a list of available currencies press /exchange.\n' +
    '2) Click on the currency you are interested in.\n' +
    '3) You will receive a message containing information regarding the source and the target currencies, ' +
                      'buying rates and selling rates.\n' + '4) Click “Update” to receive the current information regarding the request. ' +
                      'The bot will also show the difference between the previous and the current exchange rates.\n' +
                      '5) The bot supports inline. Type @<botusername> in any chat and the first letters of a currency.', reply_markup=keyboard )"""