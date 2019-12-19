class GameStat:

    def __init__(self, id, name, num_plays=0, result=0):
        self.__id = id
        self.__name = name
        self.__num_plays = num_plays
        self.__result = result

    def __str__(self):
        return f"{self.__name}: #plays = {self.__num_plays}, #win = {self.__result}"

    def set_num_plays(self):
        self.__num_plays += 1

    def set_num_result(self, win_value):
        win_value = win_value.split('; ')
        self.__result += int(win_value[1])
