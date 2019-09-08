# coding -*- utf-8 -*-
from random import randrange


class Black_jack:

    def __init__(self, bank):
        self.bank = bank

    def create_deck(self):
        return [i + j for i in VALUES for j in SUITS]

    @property
    def check_bank(self):
        return self.bank

    def show_hand(self, who, hand):
        if who == PLAYER:
            return 'You have : {}'.format(hand)
        else:
            return 'Bot have : {}'.format(hand)

    def get_winner(self):
        player = self.count_points(player_hand)
        bot = self.count_points(bot_hand)

        if player == 21 and len(bot_hand) == 1:
            self.bank += int(bet * 1.5)
            return 'BlackJack!'
        elif player > 21 or 21 >= bot > player:
            self.bank -= bet
            return 'You lose'
        elif bot > 21 or 21 >= player > bot:
            self.bank += bet
            return 'You win'
        else:
            return 'Draw'

    def get_card(self, hand):
        card = deck.pop(randrange(len(deck)))
        hand.append(card)

    def count_points(self, cards):
        points = 0

        for card in cards:
            if card[0] in '23456789':
                points += int(card[0])
            elif card[0] in '1JQK':
                points += 10

        for card in cards:
            if card[0] == 'A' and points > 10:
                points += 1
            elif card[0] == 'A' and points <= 10:
                points += 11
        return points

    def bot_turn(self):
        while black_jack.count_points(bot_hand) < 17:
            black_jack.get_card(bot_hand)
        print(black_jack.show_hand(BOT, bot_hand))


BOT = 'bot'
PLAYER = 'player'
VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♥', '♦', '♣', '♠']
HIT = 'hit'
STAND = 'stand'


if __name__ == '__main__':
    black_jack = Black_jack(1000)

    while black_jack.check_bank > 0:
        print(black_jack.check_bank)
        decision = None
        player_hand = []
        bot_hand = []
        deck = black_jack.create_deck()
        bet = int(input('Place a bet\n'))

        black_jack.get_card(player_hand)
        black_jack.get_card(player_hand)
        black_jack.get_card(bot_hand)
        print(black_jack.show_hand(PLAYER, player_hand))
        print(black_jack.show_hand(BOT, bot_hand))
        if black_jack.count_points(player_hand) != 21:
            while decision != STAND and black_jack.count_points(player_hand) < 21:
                decision = input('~ ')
                if decision == HIT:
                    black_jack.get_card(player_hand)
                    print(black_jack.show_hand(PLAYER, player_hand))
        if decision == STAND:
            black_jack.bot_turn()
        print(black_jack.get_winner())
    print('Your bank is zero!\nThis is the END!')
