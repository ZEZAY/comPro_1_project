import pygame


def create_line():
    """This modu is to create main line
    """

    lines = []
    for x in range(0, (14 * 3) + 1):
        x *= 100 / 3
        # vertical line 
        lines.append(((x + (100 / 3), 50 - (100 / 3)), (x + (100 / 3), 550 + (100 / 3))))
    for y in range(0, 6 * 3):
        y *= 100 / 3
        # horizontal line
        lines.append((((100 / 3), y + 50 - (100 / 3)), (1400 + (100 / 3), y + 50 - (100 / 3))))
    return lines


def create_line_num(st_num):
    """This modu is to create line_num
    """

    line_num = []
    num = st_num
    while num <= 36:
        line_num.append(num)
        num += 3
    return line_num


class Table:

    def __init__(self):
        self.table_lines = [
            # vertical line 
            ((100, 50), (100, 550)),
            ((200, 50), (200, 350)),
            ((300, 50), (300, 350)),
            ((400, 50), (400, 350)),
            ((500, 50), (500, 550)),
            ((600, 50), (600, 350)),
            ((700, 50), (700, 350)),
            ((800, 50), (800, 350)),
            ((900, 50), (900, 550)),
            ((1000, 50), (1000, 350)),
            ((1100, 50), (1100, 350)),
            ((1200, 50), (1200, 350)),
            ((1300, 50), (1300, 550)),
            ((1400, 50), (1400, 350)),

            ((300, 450), (300, 550)),
            ((700, 450), (700, 550)),
            ((1100, 450), (1100, 550)),

            # horizontal line
            ((50, 50), (1400, 50)),
            ((100, 150), (1400, 150)),
            ((100, 250), (1400, 250)),
            ((55, 350), (1400, 350)),
            ((100, 450), (1300, 450)),
            ((100, 550), (1300, 550)),

            # v_shapde
            ((25, 200), (50, 50)),
            ((25, 200), (50, 350)),
        ]
        self.table_hide_lines = create_line()
        self.__all_num = [num for num in range(37)]
        self.__even_num = [num for num in range(37) if num % 2 == 0]
        self.__odd_num = [num for num in range(37) if not num % 2 == 0]
        self.__red_num = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        self.__black_num = [num for num in self.get_all_num() if (num not in self.get_red_num()) and (num != 0)]
        self.__first_half_num = [num for num in range(1, 19)]
        self.__second_half_num = [num for num in range(19, 37)]
        self.__first_line_num = create_line_num(1)
        self.__second_line_num = create_line_num(2)
        self.__third_line_num = create_line_num(3)
        self.__first_set_num = [num for num in range(1, 13)]
        self.__second_set_num = [num for num in range(13, 25)]
        self.__third_set_num = [num for num in range(25, 37)]
        self.__main_table = [self.get_third_line_num(), self.get_second_line_num(), self.get_first_line_num()]
        self.__pos_chip = [100, 100]

    def get_main_table(self):
        """This modu is to get main_table lidt
        """

        return self.__main_table

    def ifpass(self):
        """This modu is to return item if position out of bet Area
        """

        self.__pos_chip = [100, 100]
        return self.__all_num, 1

    def check_selected_num(self, x, y):
        """This modu is to get input = position, check, return list of num
        """

        # out bets: h1
        if y in range(10, 13):
            if x in range(2, 14):
                self.__pos_chip = [8, 11]
                return self.__first_set_num, 2
            elif x in range(14, 26):
                self.__pos_chip = [20, 11]
                return self.__second_set_num, 2
            elif x in range(26, 38):
                self.__pos_chip = [32, 11]
                return self.__third_set_num, 2
            else:
                return self.ifpass()
        # out bets: h2
        elif y in range(13, 16):
            if x in range(2, 8):
                self.__pos_chip = [4, 14]
                return self.__first_half_num, 1
            elif x in range(8, 14):
                self.__pos_chip = [11, 14]
                return self.__even_num, 1
            elif x in range(14, 20):
                self.__pos_chip = [17, 14]
                return self.__red_num, 1
            elif x in range(20, 26):
                self.__pos_chip = [23, 14]
                return self.__black_num, 1
            elif x in range(26, 32):
                self.__pos_chip = [29, 14]
                return self.__odd_num, 1
            elif x in range(32, 38):
                self.__pos_chip = [35, 14]
                return self.__second_half_num, 1
            else:
                return self.ifpass()
        # out bets: v1
        elif x in range(38, 41):
            if y in range(1, 4):
                self.__pos_chip = [39.25, 2]
                return self.__third_line_num, 2
            elif y in range(4, 7):
                self.__pos_chip = [39.25, 5]
                return self.__second_line_num, 2
            elif y in range(7, 10):
                self.__pos_chip = [39.25, 8]
                return self.__first_line_num, 2
            else:
                return self.ifpass()
        # in bets
        elif x in range(1, 38) and y in range(0, 10):
            self.__pos_chip = [x + 0.5, y]
            if x in [1, 2]:
                if y in [0, 1]:
                    return [0, 1, 2, 3], 8
                elif y in [3, 4]:
                    return [0, 2, 3], 11
                elif y in [6, 7]:
                    return [0, 1, 2], 11
                else:
                    return self.ifpass()
            elif x % 3 == 0 or x == 37:
                if x == 37:
                    x -= 1
                if y in [0, 1, 9]:
                    return [x - 2, x - 1, x], 11
                if y == 2:
                    return [x], 35
                if y in [3, 4]:
                    return [x - 1, x], 17
                if y == 5:
                    return [x - 1], 35
                if y in [6, 7]:
                    return [x - 2, x - 1], 17
                if y == 8:
                    return [x - 2], 35
            else:
                if x % 3 == 1:
                    x -= 1
                else:
                    x -= 2

                if y in [0, 1, 9]:
                    return [x - 2, x - 1, x, x + 1, x + 2, x + 3], 5
                if y == 2:
                    return [x, x + 3], 17
                if y in [3, 4]:
                    return [x - 1, x, x + 2, x + 3], 8
                if y == 5:
                    return [x - 1, x + 2], 17
                if y in [6, 7]:
                    return [x - 2, x - 1, x + 1, x + 2], 8
                if y == 8:
                    return [x - 2, x + 1], 17
        else:
            return self.ifpass()

    def get_all_num(self):
        """This modu is to get all_num list
        """

        return self.__all_num

    def get_red_num(self):
        """This modu is to get red_num list
        """

        return self.__red_num

    def get_first_line_num(self):
        """This modu is to get first_line_num list
        """

        return self.__first_line_num

    def get_second_line_num(self):
        """This modu is to get second_line_num list
        """

        return self.__second_line_num

    def get_third_line_num(self):
        """This modu is to get third_line_num list
        """

        return self.__third_line_num

    def get_pos_chip(self):
        """This modu is to get chip position
        """

        return self.__pos_chip

    def draw_board_num(self, screen):
        """This modu is to draw number on board 
        """

        text, textRect = self.display_txt(40, ('0'), (255, 255, 255), -0.5, 1.5)
        screen.blit(text, textRect)
        for y in range(len(self.__main_table)):
            for x in range(len(self.__main_table[0])):
                if self.__main_table[y][x] in self.get_red_num():
                    screen.blit(red, (((x + .1) * 100) + 100, ((y + .1) * 100) + 50))
                else:
                    screen.blit(black, (((x + .1) * 100) + 100, ((y + .1) * 100) + 50))

                text, textRect = self.display_txt(40, (f'{self.__main_table[y][x]}'), (255, 255, 255), x + .5, y + .5)
                screen.blit(text, textRect)

        text, textRect = self.display_txt(40, ('1st 12'), (255, 255, 255), 2, 3.5)
        screen.blit(text, textRect)
        text, textRect = self.display_txt(40, ('2nd 12'), (255, 255, 255), 6, 3.5)
        screen.blit(text, textRect)
        text, textRect = self.display_txt(40, ('3rd 12'), (255, 255, 255), 10, 3.5)
        screen.blit(text, textRect)

        text, textRect = self.display_txt(40, ('1st'), (255, 255, 255), 12.5, 2.5)
        screen.blit(text, textRect)
        text, textRect = self.display_txt(40, ('2nd'), (255, 255, 255), 12.5, 1.5)
        screen.blit(text, textRect)
        text, textRect = self.display_txt(40, ('3rd'), (255, 255, 255), 12.5, 0.5)
        screen.blit(text, textRect)

        text, textRect = self.display_txt(40, ('1-18'), (255, 255, 255), 1, 4.5)
        screen.blit(text, textRect)
        text, textRect = self.display_txt(40, ('EVEN'), (255, 255, 255), 3, 4.5)
        screen.blit(text, textRect)
        text, textRect = self.display_txt(40, ('RED'), (255, 255, 255), 5, 4.5)
        screen.blit(text, textRect)
        text, textRect = self.display_txt(40, ('BLACK'), (255, 255, 255), 7, 4.5)
        screen.blit(text, textRect)
        text, textRect = self.display_txt(40, ('ODD'), (255, 255, 255), 9, 4.5)
        screen.blit(text, textRect)
        text, textRect = self.display_txt(40, ('19-36'), (255, 255, 255), 11, 4.5)
        screen.blit(text, textRect)

    def display_txt(self, font_size, txt, rgb_code, where_x, where_y):
        """This modu is to setting text to display
        """

        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render(txt, True, rgb_code)
        textRect = text.get_rect()
        textRect.center = (((where_x * 100) + 100, (where_y * 100) + 50))
        return text, textRect


black = pygame.image.load('img/roulette_img/black.PNG')
black = pygame.transform.scale(black, (80, 80))
red = pygame.image.load('img/roulette_img/red.PNG')
red = pygame.transform.scale(red, (80, 80))
chip = pygame.image.load('img/roulette_img/black-chip.png')
chip = pygame.transform.scale(chip, (80, 80))
selected_img = pygame.image.load('img/roulette_img/selected_img.PNG')
selected_img = pygame.transform.scale(selected_img, (100, 100))
run_img = pygame.image.load('img/roulette_img/running.jpg')
run_img = pygame.transform.scale(run_img, (1500, 700))
