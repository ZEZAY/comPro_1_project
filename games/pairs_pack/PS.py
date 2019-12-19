import pygame
import time
import decks

SQUARESZE_COLS = 100
SQUARESZE_ROW = 153

NUM_COLS = 5
NUM_ROW = 3

TIMEING = 120


class PS:

    def __init__(self):
        self.deck = decks.Deck()
        self.__grid_lines = [
            # vertical line 
            ((100, 0), (100, 459)),
            ((200, 0), (200, 459)),
            ((300, 0), (300, 459)),
            # horizontal line
            ((0, 153), (300, 153)),
            ((0, 306), (300, 306)),
        ]
        self.__grid = ([[0 for x in range(NUM_COLS - 2)] for y in range(NUM_ROW)])
        self.__game_over = False
        self.__deck = self.deck.initialize_cards(2)
        self.deck.shuffle_cards(self.__deck)
        self.__selected = []
        self.__select_check_ok = True
        self.__score = 0
        self.__time_start = time.time()

    def get_score(self):
        """This modu is to return score
        """

        return self.__score

    def display_txt(self, font_size: int, txt: str, rgb_code, where_x: float, where_y: float):
        """This modu is to setting text to display
        """

        font = pygame.font.Font('freesansbold.ttf', font_size)
        text = font.render(txt, True, rgb_code)
        text_rect = text.get_rect()
        text_rect.center = (where_x * SQUARESZE_COLS, where_y * SQUARESZE_ROW)
        return text, text_rect

    def draw(self, screen):
        """This modu is to draw obj on screen
        """

        if not self.__game_over:
            for line in self.__grid_lines:
                pygame.draw.line(screen, (0, 0, 0), line[0], line[1], 2)

            # display card balance
            if len(self.__deck) != 0:
                screen.blit(decks.gray_back, (3.5 * SQUARESZE_COLS, 0.25 * SQUARESZE_ROW))
                text, text_rect = self.display_txt(32, (f'{len(self.__deck)}'), (10, 50, 255), 4, 0.75)
                screen.blit(text, text_rect)

            # display score
            text, text_rect = self.display_txt(32, (f'score = {self.__score}'), (255, 255, 255), 4, 1.75)
            screen.blit(text, text_rect)

            # display time
            now_time = (TIMEING - (int(time.time() - self.__time_start)))
            text, text_rect = self.display_txt(32, (f'{now_time}'), (255, 255, 255), 4, 2.5)
            screen.blit(text, text_rect)

            # fill cards
            self.update_grid()

            # display img
            for y in range(len(self.__grid)):
                for x in range(len(self.__grid[y])):
                    if self.get_cell_value(x, y) == ['2 ♠']:
                        screen.blit(decks._2S, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['2 ♥']:
                        screen.blit(decks._2H, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['2 ♦']:
                        screen.blit(decks._2D, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['2 ♣']:
                        screen.blit(decks._2C, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['3 ♠']:
                        screen.blit(decks._3S, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['3 ♥']:
                        screen.blit(decks._3H, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['3 ♦']:
                        screen.blit(decks._3D, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['3 ♣']:
                        screen.blit(decks._3C, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['4 ♠']:
                        screen.blit(decks._4S, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['4 ♥']:
                        screen.blit(decks._4H, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['4 ♦']:
                        screen.blit(decks._4D, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['4 ♣']:
                        screen.blit(decks._4C, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['5 ♠']:
                        screen.blit(decks._5S, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['5 ♥']:
                        screen.blit(decks._5H, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['5 ♦']:
                        screen.blit(decks._5D, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['5 ♣']:
                        screen.blit(decks._5C, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['6 ♠']:
                        screen.blit(decks._6S, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['6 ♥']:
                        screen.blit(decks._6H, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['6 ♦']:
                        screen.blit(decks._6D, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['6 ♣']:
                        screen.blit(decks._6C, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['7 ♠']:
                        screen.blit(decks._7S, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['7 ♥']:
                        screen.blit(decks._7H, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['7 ♦']:
                        screen.blit(decks._7D, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['7 ♣']:
                        screen.blit(decks._7C, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['8 ♠']:
                        screen.blit(decks._8S, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['8 ♥']:
                        screen.blit(decks._8H, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['8 ♦']:
                        screen.blit(decks._8D, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['8 ♣']:
                        screen.blit(decks._8C, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['9 ♠']:
                        screen.blit(decks._9S, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['9 ♥']:
                        screen.blit(decks._9H, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['9 ♦']:
                        screen.blit(decks._9D, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['9 ♣']:
                        screen.blit(decks._9C, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['10 ♠']:
                        screen.blit(decks._10S, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['10 ♥']:
                        screen.blit(decks._10H, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['10 ♦']:
                        screen.blit(decks._10D, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['10 ♣']:
                        screen.blit(decks._10C, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['J ♠']:
                        screen.blit(decks._JS, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['J ♥']:
                        screen.blit(decks._JH, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['J ♦']:
                        screen.blit(decks._JD, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['J ♣']:
                        screen.blit(decks._JC, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['Q ♠']:
                        screen.blit(decks._QS, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['Q ♥']:
                        screen.blit(decks._QH, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['Q ♦']:
                        screen.blit(decks._QD, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['Q ♣']:
                        screen.blit(decks._QC, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['K ♠']:
                        screen.blit(decks._KS, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['K ♥']:
                        screen.blit(decks._KH, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['K ♦']:
                        screen.blit(decks._KD, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['K ♣']:
                        screen.blit(decks._KC, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['A ♠']:
                        screen.blit(decks._AS, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['A ♥']:
                        screen.blit(decks._AH, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['A ♦']:
                        screen.blit(decks._AD, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
                    elif self.get_cell_value(x, y) == ['A ♣']:
                        screen.blit(decks._AC, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))

            # display selected_img
            for y in range(len(self.__grid)):
                for x in range(len(self.__grid[y])):
                    if self.get_cell_value(x, y) in self.__selected:
                        screen.blit(decks.selected_img, (x * SQUARESZE_COLS, y * SQUARESZE_ROW))
        else:
            # display GAME OVER
            text, text_rect = self.display_txt(50, (f'GAME OVER'), (255, 0, 0), 2.5, 1.25)
            screen.blit(text, text_rect)

            # display score
            text, text_rect = self.display_txt(32, (f'score = {self.__score}'), (255, 0, 0), 2.5, 1.75)
            screen.blit(text, text_rect)

            # display txt
            text, text_rect = self.display_txt(24, (f'Tap "SPEACE BAR" to restart'), (255, 0, 0), 2.5, 2.5)
            if int(time.time()) % 2 == 0:
                screen.blit(text, text_rect)

    def update_grid(self):
        """This modu is to update grid
        """

        for y in range(len(self.__grid)):
            for x in range(len(self.__grid[y])):
                if self.get_cell_value(x, y) == 0:
                    self.set_cell_value(x, y, self.deck.draw_cards(self.__deck, 1))

    def print_grid(self):
        """This modu is to print grid
        """

        for row in self.__grid:
            print(row)

    def get_cell_value(self, x: float, y: float):
        """This modu is to get value from position (x, y)
        """

        return self.__grid[y][x]

    def set_cell_value(self, x: float, y: float, value):
        """This modu is to set position
        """

        self.__grid[y][x] = value

    def get_mouse(self, x: float, y: float):
        """This modu is to get mouse position
        """

        if x < 3:
            if self.get_cell_value(x, y) not in self.__selected:
                self.__selected.append(self.get_cell_value(x, y))
            else:
                self.__selected.remove(self.get_cell_value(x, y))
        else:
            self.check_selected()

    def check_selected(self):
        """This modu is to check selected list
        """

        if len(self.__selected) != 0 and len(self.__selected) <= 3:
            card = self.__selected[0][0].split()
            card_rank = card[0]
            card_suit = card[1]

            for card in self.__selected:
                card = card[0].split()
                if (card[0] != card_rank) and (card[1] != card_suit):
                    self.__select_check_ok = False

            if self.__select_check_ok:
                self.calculate_score(card_rank, card_suit)
            else:
                print('invalid selection')
                self.__select_check_ok = True
                self.__selected = []

        elif len(self.__selected) == 0:
            print('selected empty')
        else:
            print('invalid selection')
            self.__selected = []

    def calculate_score(self, card_rank, card_suit):
        """This modu is to calculate score
        """

        current_score = self.__score
        n = 0
        for y in range(len(self.__grid)):
            for x in range(len(self.__grid[0])):
                card_in_grid = (self.__grid[y][x][0]).split()
                if (card_in_grid[0] == card_rank) and (card_in_grid[1] == card_suit):
                    n += 1

        if len(self.__selected) == 1:
            if n == 2:
                self.__score += 7
            else:
                print('invalid selection')
        elif len(self.__selected) == 2:
            if n == 2:
                self.__score += 21
            else:
                self.__score += 3
        else:
            rank = []
            suit = []
            for card in self.__selected:
                card = card[0].split()
                rank.append(card[0])
                suit.append(card[1])
            if len(set(rank)) == 1 or len(set(suit)) == 1:
                self.__score += 15
            else:
                print('invalid selection')

        if current_score != self.__score:
            for y in range(len(self.__grid)):
                for x in range(len(self.__grid[0])):
                    if self.__grid[y][x] in self.__selected:
                        self.__grid[y][x] = 0

        self.__selected = []

    def set_game_over(self):
        """This modu is to check time and set game_over
        """

        if int(time.time() - self.__time_start) >= TIMEING:
            self.__game_over = True

    def get_game_over(self):
        """This modu is to return game_over bool
        """

        return self.__game_over

    def reset(self):
        """This modu is to reset game
        """

        self.__grid = ([[0 for x in range(NUM_COLS - 2)] for y in range(NUM_ROW)])
        self.__game_over = False
        self.__deck = self.deck.initialize_cards(2)
        self.deck.shuffle_cards(self.__deck)
        self.__selected = []
        self.__select_check_ok = True
        self.__score = 0
        self.__time_start = time.time()
