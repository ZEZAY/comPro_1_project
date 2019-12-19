import game_stat


def set_value(value):
    try:
        value = value.split('; ')
        return int(value[1])
    except:
        print('Invalid value')


def setting_base_stat_list(game_stat_list: list):
    """This modu is to create list for each game
    """

    black_stat_list = []
    pairs_stat_list = []
    roulette_stat_list = []
    for t in (game_stat_list):
        if t[0] == 'b':
            black_stat_list.append(t)
        elif t[0] == 'p':
            pairs_stat_list.append(t)
        elif t[0] == 'r':
            roulette_stat_list.append(t)
        elif t[0] == 'x':
            pass
        else:
            print('invalid score_list')
    return black_stat_list, pairs_stat_list, roulette_stat_list


def setting_base_score(game_stat_list: list):
    """This modu is to check score in game list
    """

    score = 0
    for x in (game_stat_list):
        score += int(x[3:])
    return score


class Player:
    __player_database = []
    class_name = "Player"

    def __init__(self, name: str, game_stat_list=[], score=0, balance=1000):

        self.__name = name
        self.__game_stat_list = game_stat_list
        self.__score = score
        self.__balance = balance

        black_stat_list, pairs_stat_list, roulette_stat_list = setting_base_stat_list(game_stat_list)
        self.__blackjeck = game_stat.GameStat(1, "Blackjeck", len(black_stat_list), setting_base_score(black_stat_list))
        self.__pairs = game_stat.GameStat(2, "Pairs", len(pairs_stat_list), setting_base_score(pairs_stat_list))
        self.__roulette = game_stat.GameStat(3, "Roulette", len(roulette_stat_list),
                                             setting_base_score(roulette_stat_list))

        self.__player_database.append(self)

    def search_account(self):
        """This modu is to ckeck if have this player in database
        """

        for i in range(len(self.__player_database)):
            if self.__player_database[i].__name == self.__name:
                return i
        print("AccountNotFound")

    def find_game_stat(self, game_id):
        """This modu is to find game class
        """

        if game_id == 1:
            return self.__blackjeck
        elif game_id == 2:
            return self.__pairs
        elif game_id == 3:
            return self.__roulette
        else:
            print('Invalid game_id')

    # เรียกหลังจบเกม
    def update_num_result(self, game_id, value):
        """This modu is to update number of result for All games
        """

        self.update_num_plays(game_id)
        game = self.find_game_stat(game_id)
        game.set_num_result(value)
        self.update_game_stat_list(value)
        self.update_balance(value)

    def update_num_plays(self, game_id):
        """This modu is to update number of times that play a game 
        """

        game = self.find_game_stat(game_id)
        game.set_num_plays()

    def update_game_stat_list(self, win_value):
        """This modu is to update list of game_stat_list for All games
        """

        self.__game_stat_list.append(win_value)

    def update_balance(self, payment):
        """This modu is to update balance of payment for Roulette game
        """

        try:
            if isinstance(payment, str):
                payment = set_value(payment)
            self.search_account()
            self.__balance += payment
        except:
            print("AccountNotFound")

    def __str__(self):
        string = f"{self.__name}: Balance = {self.__balance:.2f}\n{self.__blackjeck}\n{self.__pairs}\n{self.__roulette}"
        return string

    @classmethod
    def all_player(cls):
        """This modu is to create list of all data
        """

        all_data = []
        for a_player in cls.__player_database:
            all_data.append(str(a_player) + '\n' + 'game_stat_list: ' + str(a_player.__game_stat_list))
        return all_data

    @classmethod
    def show_all_player(cls):
        """This modu is to print all players data
        """

        for a_player in cls.__player_database:
            print()
            print(a_player)

    @classmethod
    def show_a_player(cls, name):
        """This modu is to print a player data, use input player's name
        """

        for a_player in cls.__player_database:
            if a_player.__name == name:
                print()
                print(a_player)

    @classmethod
    def get_player_database(cls):
        """This modu is to return class player database
        """

        return cls.__player_database

    @classmethod
    def all_player_name(cls):
        """This modu is to  create list of players name
        """

        players_name = []
        for a_player in cls.__player_database:
            players_name.append(a_player.__name)
        return players_name
