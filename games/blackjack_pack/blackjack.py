import sys

sys.path.insert(1, 'players/')
import players_handler
from BJ import *


def main():
    BJ = Bj()
    end_game = False
    win, loose, tie, time = 0, 0, 0, 0
    while not end_game:
        time += 1
        this_game_end = False
        player_draw_more = True
        com_draw_more = True
        player_hand = []
        com_hand = []

        print(f"\nLet's play Blackjack! Round #{time}")
        deck = BJ.initialize_cards(1)
        BJ.shuffle_cards(deck)

        while com_draw_more or player_draw_more:

            if player_draw_more:
                player_hand += BJ.draw_cards(deck, 1)
                print("Your hand:", BJ.display_cards(player_hand))
                player_hand_value = BJ.calculate_hand_value(player_hand)
                if player_hand_value > 21:
                    print("You loose!")
                    loose += 1
                    this_game_end = True
                    break
                player_draw_more = BJ.must_draw_more(player_hand_value)

            if com_draw_more:
                com_hand += BJ.draw_cards(deck, 1)
                print("Computer hand:", BJ.display_cards(com_hand))
                com_hand_value = BJ.calculate_hand_value(com_hand)
                if com_hand_value > 21:
                    print("You win!")
                    win += 1
                    this_game_end = True
                    break
                elif com_hand_value == 21:
                    print("You loose!")
                    tie += 1
                    this_game_end = True
                    break
                com_draw_more = BJ.com_must_draw_more(com_hand_value, player_hand_value)

        if not this_game_end:
            win, loose, tie = BJ.check_winner(player_hand_value, com_hand_value, win, loose, tie)

        q = input("Play a new round (Y/N): ").lower()
        if q != 'y':
            end_game = True

    score = ((win * 50) + (loose * (-50)) + (tie * 25))
    return int(score)
