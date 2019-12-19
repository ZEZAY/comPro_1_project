import sys

sys.path.insert(1, 'players/')
import players_handler
import player

sys.path.insert(1, 'games/pairs_pack')
import pairs

sys.path.insert(1, 'games/blackjack_pack')
import blackjack

sys.path.insert(1, 'games/roulette_pack')
import roulette

me = players_handler.PlayersHandler()


def ask_for_player_type():
    """This modu is to get player_type as admin/player
    """

    player_type = 'unknow'
    while player_type != 'admin' and player_type != 'player':
        player_type = input('\nEnter your status (admin/player): ').lower()
    return player_type


def ask_for_player_name():
    """This modu is to get player_name (must be in database)
    """

    player_name = 'unknow'
    me.read_from_file('player_stat')
    while not (player_name in players_handler.player.Player.all_player_name()):
        player_name = input('Enter your name: ')
    return player_name


def select_choice(n: int):
    """This modu is to get choose in range n
    """

    choose = '0'
    while not choose in [str(x) for x in range(1, n + 1)]:
        choose = input('You choose ')
    return int(choose)


def get_toquit():
    """This modu is to get toquit value as m/q
    """

    toquit = 'unknow'
    while toquit != 'm' and toquit != 'q':
        toquit = input('Back to Main or Quit (M/Q): ').lower()
    return toquit


def run_for_player():
    """This modu is to run progarm as a player
    """

    person_name = ask_for_player_name()
    while True:
        print(
            "\nSelect your choice\n1. Play Blackjack\n2. Play Pairs\n3. Play Roulette\n4. See your profile\n5. Stop playing")
        choice = select_choice(5)
        if choice == 1:
            score = blackjack.main()
            print(f"\nYou Got 'score = {score}'")
            me.update_game_play(person_name, 1, f'r; {score}')

        elif choice == 2:
            score = pairs.main()
            print(f"\nYou Got 'score = {score}'")
            me.update_game_play(person_name, 2, f'p; {score}')

        elif choice == 3:
            score = roulette.main()
            print(f"\nYou Got 'score = {score}'")
            me.update_game_play(person_name, 3, f'r; {score}')

        elif choice == 4:
            me.read_from_file('player_stat')
            player.Player.show_a_player(person_name)
        else:
            return False


def run_for_admin():
    """This modu is to run progarm as an admin
    """

    while True:
        print("\n1. Add new player\n2. Show players\n3. Add player's balance\n4. Quit")
        choice = select_choice(4)
        if choice == 1:
            name = input("\nNew player name: ")
            try:
                money = float(input("New player balance: "))
            except:
                print("INVALID VALUE")
                print("-> Please check your input")
            me.add_new_player(name, money)
        elif choice == 2:
            me.read_from_file('player_stat')
            player.Player.show_all_player()
        elif choice == 3:
            name = input("\nAdd to who?: ")
            try:
                money = float(input("How much?: "))
            except:
                print("INVALID VALUE")
            try:
                me.add_balance(name, money)
                print(f"{money:.2f} has added to '{name}'")
            except:
                print("-> Please check your input")
        else:
            return False


def main():
    while True:
        person_type = ask_for_player_type()
        still_run = True
        while still_run:
            if person_type == 'player':
                still_run = run_for_player()
            else:
                still_run = run_for_admin()

        toquit = get_toquit()
        if toquit == 'q':
            print("\nEnjoy next time, Bye")
            break
