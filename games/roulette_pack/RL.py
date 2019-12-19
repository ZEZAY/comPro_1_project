import pygame
import time
import random
import tables

SQUARESZE_COLS = 100
SQUARESZE_ROW = 100

NUM_COLS = 15
NUM_ROW = 7

TIMEING = 15
WAITTING = 10


class RL:

    def __init__(self):
        self.table = tables.Table()
        self.__grid_lines = self.table.table_lines
        self.__grid_hide_lines = self.table.table_hide_lines
        self.__game_over = False
        self.__time_start = time.time()
        self.__time_wait_start = 0
        self.__selected_list = []
        self.__betrate = 1
        self.__win_num = 'unknow'
        self.__score = 0

    def get_score(self):
        """This modu is to return score
        """

        return self.__score

    def get_selected_list(self):
        """This modu is to get selected list
        """

        return self.__selected_list

    def display_txt(self, font_size, txt, rgb_code, where_x, where_y):
        """This modu is to setting text to display
        """

        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render(txt, True, rgb_code)
        textRect = text.get_rect()
        textRect.center = (where_x * SQUARESZE_COLS, where_y * SQUARESZE_ROW)
        return text, textRect

    def draw(self, screen):
        """This modu is to draw obj on screen
        """

        if not self.__game_over:
            # for line in self.__grid_hide_lines:
            #     pygame.draw.line(screen, (255, 0, 0), line[0], line[1], 2)

            for line in self.__grid_lines:
                pygame.draw.line(screen, (255, 255, 255), line[0], line[1], 2)

            # draw boart number
            self.table.draw_board_num(screen)

            # display selected img
            for y in range(len(self.table.get_main_table())):
                for x in range(len(self.table.get_main_table()[0])):
                    if self.table.get_main_table()[y][x] in self.__selected_list:
                        screen.blit(tables.selected_img, (((x) * 100) + 100, ((y) * 100) + 50))

            # display chip img
            if self.__selected_list != []:
                x, y = int(self.table.get_pos_chip()[0] * (100 / 3)), int((self.table.get_pos_chip()[1] * (100 / 3)))
                screen.blit(tables.chip, (x, y))

            # display time
            now_time = (TIMEING - (int(time.time() - self.__time_start)))
            text, textRect = self.display_txt(32, (f'time out in {now_time}'), (255, 255, 255), 12, 6.5)
            screen.blit(text, textRect)

        elif int(time.time() - self.__time_wait_start) <= 3:
            screen.blit(tables.run_img, (0, 0))

            # display GAME OVER
            text, textRect = self.display_txt(50, (f'WAIT'), (255, 0, 0), (12), (1.5))
            screen.blit(text, textRect)

            # display txt
            text, textRect = self.display_txt(24, (f'Roulette is rolling...'), (255, 0, 0), (12), (2))
            if int(time.time()) % 2 == 0:
                screen.blit(text, textRect)

        else:
            screen.blit(tables.run_img, (0, 0))

            # display txt
            text, textRect = self.display_txt(50, (f'We Got "{self.__win_num}"'), (255, 0, 0), (12), (1.75))
            screen.blit(text, textRect)
            if self.__win_num in self.__selected_list:
                txt = f'You win x{self.__betrate}'
            else:
                txt = 'You lose'
            text, textRect = self.display_txt(30, txt, (255, 0, 0), (12), (2.5))
            screen.blit(text, textRect)
            text, textRect = self.display_txt(28, (
                f'Game will rerun in {WAITTING - (int(time.time() - self.__time_wait_start))}'), (255, 0, 0), (12), (3))
            screen.blit(text, textRect)
            text, text_rect = self.display_txt(18, (f'Tap "SPEACE BAR" to QUIT playing'), (255, 0, 0), 12, 3.5)
            if int(time.time()) % 2 == 0:
                screen.blit(text, text_rect)
                time.sleep(0.25)

    def get_mouse(self, x: float, y: float):
        """This modu is to get mouse position
        """

        self.__selected_list = []
        select_list, rate = self.table.check_selected_num(x, y)
        for num in select_list:
            self.__selected_list.append(num)
        self.__betrate = rate

    def set_game_over(self):
        """This modu is to check time and set game_over
        """

        if int(time.time() - self.__time_start) >= TIMEING:
            self.__game_over = True
            self.__time_wait_start = time.time()

            self.check_random()

    def set_time_over(self):
        """This modu is to check time and set game_over
        """

        if self.__game_over:
            self.__time_start = time.time()
            if int(time.time() - self.__time_wait_start) >= WAITTING:
                self.__game_over = False
                self.reset()

    def get_game_over(self):
        """This modu is to get game_over
        """

        return self.__game_over

    def random_num(self):
        """This modu is to random a number from 0 to 36
        """

        return random.randrange(0, 37)

    def check_random(self):
        """This modu is to check random number that in selected list or not
        """

        self.__win_num = self.random_num()
        if self.__win_num in self.__selected_list:
            self.__score += self.__betrate * 100
        else:
            self.__score -= 100

    def reset(self):
        """This modu is to restart game
        """

        self.__selected_list = []
        self.__betrate = 1
        self.__win_num = 'unknow'
