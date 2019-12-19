import player


class PlayersHandler:

    def __init__(self):
        pass

    def read_from_file(self, filename: str):
        """This modu is to read and create player data
        """

        try:
            players_name_list = []
            players_balance_list = []
            players_stat_list = []
            file = open(f'text/{filename}.txt').read()
            lines = file.splitlines()
            for i in range(len(lines)):
                txt = lines[i].split(': ')
                if i % 6 == 0:
                    players_name_list.append(txt[0])
                    txt = txt[1].split()
                    players_balance_list.append(float(txt[2]))
                elif i in [x for x in range(4, len(lines)) if (x - 4) % 6 == 0]:
                    txt = txt[1][1:len(txt[1]) - 1]
                    txt = txt.split(", ")
                    lis = []
                    for i in txt:
                        x = i[1:-1]
                        lis.append(x)
                    players_stat_list.append((lis))
                else:
                    pass

            for i in range(len(players_name_list)):
                name = players_name_list[i]
                game_stat_list = players_stat_list[i]
                score = 0
                for x in (game_stat_list):
                    score += int(x[3:])
                balance = players_balance_list[i]
                if not (name in player.Player.all_player_name()):
                    players_name_list[i] = player.Player(name, game_stat_list, score, balance)
        except:
            print('ReadFileError')

    def write_to_file(self, filename: str):
        """This modu is to write player data to txt-file
        """

        string = ""
        for player_data in player.Player.all_player():
            string += str(player_data) + '\n\n'
        file = open(f'text/{filename}.txt', 'w')
        file.write(string)
        file.close()

    def show_players_data(self):
        """This modu is to print all players data
        """

        self.read_from_file('player_stat')
        for i in player.Player.all_player():
            print()
            print(i)

    def add_new_player(self, name: str, balance: float):
        """This modu is to create a new player
        """

        self.read_from_file('player_stat')
        if not (name in player.Player.all_player_name()):
            name = player.Player(name, ['x; 0'], 0, balance)
            self.write_to_file('player_stat')
        else:
            print("'THIS NAME HAS BEEN USED'")

    def search_player(self, name: str):
        """This modu is to search and raturn player index from databaes
        """

        for i in range(len(player.Player.all_player_name())):
            if player.Player.all_player_name()[i] == name:
                return i
        print("AccountNotFound")

    def add_balance(self, name: str, added: float):
        """This modu is to add player balance
        """

        self.read_from_file('player_stat')
        player.Player.get_player_database()[self.search_player(name)].update_balance(added)
        self.write_to_file('player_stat')

    # basic call
    def update_game_play(self, name: str, game_id: int, value: str):
        """This modu is to update a game play
        """

        try:
            self.read_from_file('player_stat')
            player.Player.get_player_database()[self.search_player(name)].update_num_result(game_id, value)
            self.write_to_file('player_stat')
        except:
            print("invalid input")
