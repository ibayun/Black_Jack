import random
import itertools
import requests
import time
import telebot
from telebot import types

TOKEN = "925351426:AAHzTYMJXTZOxlqlohzdF-IEJKpUKyfOIuk"
YOUR_CHOICE = [1]


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет.'
                                      ' Опять ты меня разбудил. '
                                      'Или не ты... Сейчас не об этом. '
                                      'Ты ведь тут в картишки перебросить? '
                                      'Тогда нажимай - /start_games !. И помни - на принятие решения'
                                      ' у тебя есть 3 секунды'
                                      'Если забыл правила - /rules (специально для тебя собрал)')


@bot.callback_query_handler(func=lambda call: True)
def echo_all(call):
    print(call.data)
    if int(call.data) == 1:
        YOUR_CHOICE.append(1)
    else:
        YOUR_CHOICE.append(2)


@bot.message_handler(commands=["start_games"])
def handle_answer(message):
    bot.send_message(
        message.chat.id, "игра начинается"
    )

    def game():
        deck = develop_deck()
        hand_gamer = []
        hand_dialer = []
        hand_gamer.append(deck[-1])
        deck.pop()
        hand_gamer.append(deck[-1])
        deck.pop()
        hg = [' '.join(i) for i in hand_gamer]
        bot.send_message(
            message.chat.id, f'твои карты-  {hg}'
        )

        hand_dialer.append(deck[-1])
        deck.pop()
        hd = [' '.join(i) for i in hand_dialer]
        bot.send_message(
            message.chat.id, f'карты дилера-  {hd}'
        )
        count_gamer = count_score(hand_gamer)
        if count_gamer == 21:
            bot.send_message(
                message.chat.id, "У тебя комбинация - БЛЭК-ДЖЭК! Это красивая победа!"
            )
            print("you win! black-jack!!!")
        else:
            choise_next_step(hand_gamer, hand_dialer, deck)

    def choise_next_step(hand_gamer, hand_diler, deck):
        markup = types.InlineKeyboardMarkup(row_width=2)
        itembtn1 = types.InlineKeyboardButton('взять карту', callback_data="1")
        itembtn2 = types.InlineKeyboardButton('достаточно', callback_data="2")
        markup.add(itembtn1, itembtn2)
        bot.send_message(message.chat.id, "Выберите действие", reply_markup=markup)
        time.sleep(3)
        choice = YOUR_CHOICE[-1]
        if choice == 1:
            hand_gamer.append(deck[-1])
            deck.pop()
            print('your cards', hand_gamer)
            hg = [' '.join(i) for i in hand_gamer]
            bot.send_message(
                message.chat.id, f'твои карты-  {hg}'
            )
            check_your_score = count_score(hand_gamer)
            if check_your_score > 21:
                print("sorry. you lost")
                bot.send_message(
                    message.chat.id, 'партия проиграна. еще раз? /start_games'
                )
            elif check_your_score == 21:
                enough(hand_gamer, hand_diler, deck)
            else:
                choise_next_step(hand_gamer, hand_diler, deck)
        else:
            enough(hand_gamer, hand_diler, deck)

    def enough(hand_gamer, hand_diler, deck):
        sum_diler = count_score(hand_diler)
        sum_gamer = count_score(hand_gamer)
        if sum_diler < 17:
            hand_diler.append(deck[-1])
            deck.pop()
            print('cards diler', hand_diler)
            hd = [' '.join(i) for i in hand_diler]
            bot.send_message(
                message.chat.id, f'карты дилера-  {hd}'
            )
            enough(hand_gamer, hand_diler, deck)
        elif sum_diler > 21:
            print("you win")
            bot.send_message(
                message.chat.id, 'поздравляю с победой. еще раз? /start_games'
            )
        elif sum_diler > sum_gamer:
            print("diler win")
            bot.send_message(
                message.chat.id, 'диллер выиграл. еще раз? /start_games'
            )
        elif sum_diler == sum_gamer:
            print("push")
            bot.send_message(
                message.chat.id, 'ничья. еще раз? /start_games'
            )
        else:
            print("you win")
            bot.send_message(
                message.chat.id, 'Вы выиграли, поздравляю. еще раз? /start_games'
            )

    def count_score(*hand):
        interpreter_carts = []
        list_for_count = []

        for i in hand:
            for j in i:
                for k in j:
                    interpreter_carts.append(k)
        interpreter_car = interpreter_carts[::2]

        for n, i in enumerate(interpreter_car):
            if i == 'King' or i == 'Jack' or i == 'Queen':
                list_for_count.append(10)
            elif i == 'Ace':
                list_for_count.append(11)
            else:
                list_for_count.append(int(i))
        count_gamer = sum(list_for_count)
        return count_gamer

    def develop_deck():
        a = ('Jack', 'Queen', 'King', "Ace", "2", "3", '4', '5', '6', '7', '8', '9',)
        b = ('♥', '♦', '♣', '♠')
        d = [(i, j) for i in a for j in b]
        random.shuffle(d)
        deck_two = d
        return deck_two

    game()


@bot.message_handler(commands=["rules"])
def handle_answer(message):
    bot.send_message(
        message.chat.id, "Дилер раздает две карты игроку и одну себе."
                         "Если у игрока сразу после раздачи набралось 21 очко "
                         "(то есть у игрока туз и десятиочковая карта), то такая ситуация"
                         " и называется блек-джек. Далее игрокам,"
                         " у которых не блек-джек, предлагается на выбор либо взять ещё карту "
                         "(в таком случае игрок должен сказать дилеру «взять карту» ),"
                         " либо остаться при тех картах (и той сумме очков), которые у него на руке "
                         "(в этом случае игрок должен сказать дилеру «достаточно»).Как правило, "
                         "если у игрока после взятия новой карты в сумме получается 21, дилер не спрашивает"
                         " его больше. Если у игрока после взятия новой "
                         "карты сумма очков превысит 21, то такая ситуация называется «перебор». Игрок проигрывает."
                         "Если у дилера "
                         "в первых двух картах набирается 21 очко (блек-джек), игрок проигрывает. "

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
    if "/" in message.text:
        bot.send_message(message.chat.id, "{} - комманда не существует. Попробуй /help".format(message.text))
    else:
        pass


if __name__ == "__main__":
    bot.polling(none_stop=True)