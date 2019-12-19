import pygame


class Deck:

    def __init__(self):
        self.__RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.__SUITS = ['\u2660', '\u2665', '\u2666', '\u2663']

    def initialize_cards(self, n) -> list:
        """This Modu is use to create card deck. Return list of card with rank and suit which is 
        """

        deck = []
        for i in range(n):
            for rank in self.__RANKS:
                for suit in self.__SUITS:
                    card = rank + ' ' + suit
                    deck += [card]
        return deck

    def shuffle_cards(self, deck: list):
        """This Modu is to shuffle deck of cards
        """

        import random
        n = len(deck)
        for i in range(n):
            r = random.randrange(i, n)
            temp = deck[r]
            deck[r] = deck[i]
            deck[i] = temp

    def draw_cards(self, deck: list, n: int) -> list:
        """This Modu is to draw (n)umber of cards from the top of deck
        """

        get_cards = []
        for each_card in range(n):
            get_cards.append(deck[0])
            deck.remove(deck[0])
        return get_cards


gray_back = pygame.image.load('img/pairs_img/gray_back.png')
gray_back = pygame.transform.scale(gray_back, (100, 153))
selected_img = pygame.image.load('img/pairs_img/selected_img.png')
selected_img = pygame.transform.scale(selected_img, (100, 153))
_2S = pygame.image.load('img/pairs_img/2S.png')
_2S = pygame.transform.scale(_2S, (100, 153))
_2H = pygame.image.load('img/pairs_img/2H.png')
_2H = pygame.transform.scale(_2H, (100, 153))
_2D = pygame.image.load('img/pairs_img/2D.png')
_2D = pygame.transform.scale(_2D, (100, 153))
_2C = pygame.image.load('img/pairs_img/2C.png')
_2C = pygame.transform.scale(_2C, (100, 153))
_3S = pygame.image.load('img/pairs_img/3S.png')
_3S = pygame.transform.scale(_3S, (100, 153))
_3H = pygame.image.load('img/pairs_img/3H.png')
_3H = pygame.transform.scale(_3H, (100, 153))
_3D = pygame.image.load('img/pairs_img/3D.png')
_3D = pygame.transform.scale(_3D, (100, 153))
_3C = pygame.image.load('img/pairs_img/3C.png')
_3C = pygame.transform.scale(_3C, (100, 153))
_4S = pygame.image.load('img/pairs_img/4S.png')
_4S = pygame.transform.scale(_4S, (100, 153))
_4H = pygame.image.load('img/pairs_img/4H.png')
_4H = pygame.transform.scale(_4H, (100, 153))
_4D = pygame.image.load('img/pairs_img/4D.png')
_4D = pygame.transform.scale(_4D, (100, 153))
_4C = pygame.image.load('img/pairs_img/4C.png')
_4C = pygame.transform.scale(_4C, (100, 153))
_5S = pygame.image.load('img/pairs_img/5S.png')
_5S = pygame.transform.scale(_5S, (100, 153))
_5H = pygame.image.load('img/pairs_img/5H.png')
_5H = pygame.transform.scale(_5H, (100, 153))
_5D = pygame.image.load('img/pairs_img/5D.png')
_5D = pygame.transform.scale(_5D, (100, 153))
_5C = pygame.image.load('img/pairs_img/5C.png')
_5C = pygame.transform.scale(_5C, (100, 153))
_6S = pygame.image.load('img/pairs_img/6S.png')
_6S = pygame.transform.scale(_6S, (100, 153))
_6H = pygame.image.load('img/pairs_img/6H.png')
_6H = pygame.transform.scale(_6H, (100, 153))
_6D = pygame.image.load('img/pairs_img/6D.png')
_6D = pygame.transform.scale(_6D, (100, 153))
_6C = pygame.image.load('img/pairs_img/6C.png')
_6C = pygame.transform.scale(_6C, (100, 153))
_7S = pygame.image.load('img/pairs_img/7S.png')
_7S = pygame.transform.scale(_7S, (100, 153))
_7H = pygame.image.load('img/pairs_img/7H.png')
_7H = pygame.transform.scale(_7H, (100, 153))
_7D = pygame.image.load('img/pairs_img/7D.png')
_7D = pygame.transform.scale(_7D, (100, 153))
_7C = pygame.image.load('img/pairs_img/7C.png')
_7C = pygame.transform.scale(_7C, (100, 153))
_8S = pygame.image.load('img/pairs_img/8S.png')
_8S = pygame.transform.scale(_8S, (100, 153))
_8H = pygame.image.load('img/pairs_img/8H.png')
_8H = pygame.transform.scale(_8H, (100, 153))
_8D = pygame.image.load('img/pairs_img/8D.png')
_8D = pygame.transform.scale(_8D, (100, 153))
_8C = pygame.image.load('img/pairs_img/8C.png')
_8C = pygame.transform.scale(_8C, (100, 153))
_9S = pygame.image.load('img/pairs_img/9S.png')
_9S = pygame.transform.scale(_9S, (100, 153))
_9H = pygame.image.load('img/pairs_img/9H.png')
_9H = pygame.transform.scale(_9H, (100, 153))
_9D = pygame.image.load('img/pairs_img/9D.png')
_9D = pygame.transform.scale(_9D, (100, 153))
_9C = pygame.image.load('img/pairs_img/9C.png')
_9C = pygame.transform.scale(_9C, (100, 153))
_10S = pygame.image.load('img/pairs_img/10S.png')
_10S = pygame.transform.scale(_10S, (100, 153))
_10H = pygame.image.load('img/pairs_img/10H.png')
_10H = pygame.transform.scale(_10H, (100, 153))
_10D = pygame.image.load('img/pairs_img/10D.png')
_10D = pygame.transform.scale(_10D, (100, 153))
_10C = pygame.image.load('img/pairs_img/10C.png')
_10C = pygame.transform.scale(_10C, (100, 153))
_JS = pygame.image.load('img/pairs_img/JS.png')
_JS = pygame.transform.scale(_JS, (100, 153))
_JH = pygame.image.load('img/pairs_img/JH.png')
_JH = pygame.transform.scale(_JH, (100, 153))
_JD = pygame.image.load('img/pairs_img/JD.png')
_JD = pygame.transform.scale(_JD, (100, 153))
_JC = pygame.image.load('img/pairs_img/JC.png')
_JC = pygame.transform.scale(_JC, (100, 153))
_QS = pygame.image.load('img/pairs_img/QS.png')
_QS = pygame.transform.scale(_QS, (100, 153))
_QH = pygame.image.load('img/pairs_img/QH.png')
_QH = pygame.transform.scale(_QH, (100, 153))
_QD = pygame.image.load('img/pairs_img/QD.png')
_QD = pygame.transform.scale(_QD, (100, 153))
_QC = pygame.image.load('img/pairs_img/QC.png')
_QC = pygame.transform.scale(_QC, (100, 153))
_KS = pygame.image.load('img/pairs_img/KS.png')
_KS = pygame.transform.scale(_KS, (100, 153))
_KH = pygame.image.load('img/pairs_img/KH.png')
_KH = pygame.transform.scale(_KH, (100, 153))
_KD = pygame.image.load('img/pairs_img/KD.png')
_KD = pygame.transform.scale(_KD, (100, 153))
_KC = pygame.image.load('img/pairs_img/KC.png')
_KC = pygame.transform.scale(_KC, (100, 153))
_AS = pygame.image.load('img/pairs_img/AS.png')
_AS = pygame.transform.scale(_AS, (100, 153))
_AH = pygame.image.load('img/pairs_img/AH.png')
_AH = pygame.transform.scale(_AH, (100, 153))
_AD = pygame.image.load('img/pairs_img/AD.png')
_AD = pygame.transform.scale(_AD, (100, 153))
_AC = pygame.image.load('img/pairs_img/AC.png')
_AC = pygame.transform.scale(_AC, (100, 153))
