import telebot
import requests

TOKEN = "925351426:AAHzTYMJXTZOxlqlohzdF-IEJKpUKyfOIuk"


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["test"])
def handle_answer(message):
    print(message.text)
    bot.send_message(
        message.chat.id, message.text
    )


@bot.message_handler(content_types=["text"])
def handle_answer(message):
    print(dir(message.text))
    bot.send_message(
        message.chat.id, message.text
    )


if __name__ == "__main__":
    bot.polling(none_stop=True)
