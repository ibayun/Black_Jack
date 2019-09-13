import telebot
import requests

TOKEN = "925351426:AAHzTYMJXTZOxlqlohzdF-IEJKpUKyfOIuk"


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет.'
                                      ' Опять ты меня разбудил. '
                                      'Или не ты... Сейчас не об этом. '
                                      'Ты ведь тут в картишки перебросить? '
                                      'Тогда нажимай - /start_games !'
                                      'Если забыл правила - /rules (специально для тебя собрал')


@bot.message_handler(commands=["start_games"])
def handle_answer(message):
    bot.send_message(
        message.chat.id, "должна начаться игра"
    )


@bot.message_handler(commands=["rules"])
def handle_answer(message):
    bot.send_message(
        message.chat.id, "правила:"
    )


@bot.message_handler(commands=["help"])
def handle_answer(message):
    bot.send_message(
        message.chat.id, "Бот создан для игры в блэк джек. "
                         "Чтобы начать игру нажми - /start_games,"
                         " чтобы вспомнить правила игры - /rules,"
                         " получить помощь - /help (Сейчас ты читаешь содержимое раздела помощи."
                         " И, если понятнее не стало, обращайся сюда @AlexKhaliman, или сюда @i_bayun)"
    )


@bot.message_handler(content_types=["text"])
def handle_answer(message):
    if "/" in  message.text:
        # print(dir(message.text), "- не существует. Попробуй /help")
        bot.send_message(message.chat.id, "{} - комманда не существует. Попробуй /help".format(message.text))
    else:
        pass


if __name__ == "__main__":
    bot.polling(none_stop=True)
