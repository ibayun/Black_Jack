# coding -*- utf-8 -*-
#!python3
from random import randrange


class Black_jack:
    def __init__(self):
        self.cards = [i + j for i in VALUES for j in SUITS ]

    def get_card(self, who):
        card = self.cards.pop(randrange(len(self.cards)))
        if who == 'player':
            player_hand.append(card)
        else:
            bot_hand.append(card)


VALUES = ['2', '3', '4', '5', '6', '7',
'8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♥', '♦', '♣', '♠']


if __name__ == '__main__':
    player_hand = []
    bot_hand = []

    black_jack = Black_jack()
    black_jack.get_card('player')
    black_jack.get_card('player')
    black_jack.get_card('bot')
    print('Your cards: {} and {}'.format(player_hand[0], player_hand[1]))
    print("Bot's cards: {} and ?".format(bot_hand[0]))
