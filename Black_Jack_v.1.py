import random
import sys
import os
import time


# меню
def intro():
    print('''\n
    For calling help, press ~H~
    For starting game, press ~G~
    To buy chips, press ~B~
    ''')

def buy_chips():
    while True:
        try:
            player_cash = int(input('\nEnter amount: ').lower())
            if player_cash <= 1:
                print('Buy more than one chip.')
            else:
                break
        except ValueError:
            print("That was not a number!")
    return player_cash


# player turn
def player_turn():
    player_cards = []
    for x in range(2):
        player_cards.append(random.choice(list(cards_dict.keys())))
    card_score = [cards_dict[k] for k in player_cards if k in cards_dict]
    player_sum_point = sum(card_score)
    print('Your cards are:', player_cards, ',that\'s:', player_sum_point, 'points.')
    another_card = str(input('Another card or stop?\n').lower())
    while another_card == '1':
        player_cards.append(random.choice(list(cards_dict.keys())))
        card_score = [cards_dict[k] for k in player_cards if k in cards_dict]
        player_sum_point = sum(card_score)
        print(player_cards)
        print('Your cards are:', player_cards, ',that\'s:', player_sum_point, 'points.')
        if player_sum_point > 21:
            print(f'You lose!')
            break
        elif player_sum_point == 21:
            print(f'You win! ')
        else:
            another_card = str(input('Another card or stop?\n').lower())
    print(f'You have finished dealing cards with {player_sum_point} points')
    return player_sum_point


# bot turn
def bot_turn():
    bot_l = 0
    bot_cards = []
    bot_cards.append(random.choice(list(cards_dict.keys())))
    card_score = [cards_dict[k] for k in bot_cards if k in cards_dict]
    bot_sum_point = sum(card_score)
    print(bot_cards)
    print(bot_sum_point)
    while bot_sum_point < 21:
        bot_cards.append(random.choice(list(cards_dict.keys())))
        card_score = [cards_dict[k] for k in bot_cards if k in cards_dict]
        bot_sum_point = sum(card_score)
        print(bot_cards)
        print('Dealer\'s cards are:', bot_cards, ',that\'s:', bot_sum_point, 'points.')
        if bot_sum_point > 21:
            print(f'Dealer lose!')
            bot_l += 1
            break
        elif bot_sum_point == 21:
            print(f'Dealer win! ')
            break
        elif bot_sum_point > player_sum_point and bot_sum_point < 21:
            print(f'Dealer win! ')
            break
        elif bot_sum_point < player_sum_point:
            print(f'Dealer loses!')
            bot_l += 1
            break
        elif bot_sum_point > 21  and player_sum_point > 21:
            bot_l += 0
            break

    return bot_wins


cards_dict = dict(Two=2, Three=3, Four=4, Five=5, Six=6, Seven=7, Eight=8, Nine=9, Ten=10, Jack=10, Queen=10, King=10,
                  Ace=11)

player_cash = 0
win_lose = 0

print('\nHello, it\'s card game - Black Jack!')

while True:
    intro()
    start = str(input('\nCommand: ').lower())
    if start == 'b':
        player_cash = buy_chips()
    if start == 'h':
        print("Rules: https://en.wikipedia.org/wiki/Blackjack")
    while start == 'g':
        while True:
            player_bid = int(input('Make your bid: '))
            if player_bid > player_cash:
                print("Not enough money.")
                continue
            else:
                break
        player_cash = player_cash - player_bid
        os.system('cls')
        print('Your chips:', player_cash, '\nYour bid: ', player_bid, '\nYou won', win_lose, 'times!')

        while True:
            pc = str(input('Take a card? press ~T~\n').lower())
            if pc == 't':
                player_sum_point = player_turn()
            elif pc != 't':
                continue
            print('\nBot turn!')
            bot_wins = bot_turn()
            win_lose += bot_wins
            break

        start = str(input('\nNew game: ').lower())





