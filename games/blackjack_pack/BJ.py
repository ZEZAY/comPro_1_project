import error


class Bj:
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

    def validate_hand(self, hand) -> bool:
        """Return True if this hand is valid, return False, otherwise.
        """

        for each_card in hand:
            ltemp = each_card.split()
            try:
                if not (ltemp[0] in self.__RANKS):
                    raise error.InvalidCardRank
                if not (ltemp[1] in self.__SUITS):
                    raise error.InvalidCardSuit
            except error.InvalidCardRank:
                print("Found this invalid rank", ltemp[0], "; rank must be in", self.__RANKS)
                return False
            except error.InvalidCardSuit:
                print("Found this invalid suit", ltemp[1], "; suite must be in", self.__SUITS)
                return False
        return True

    def display_cards(self, lcards: list) -> str:
        """This Modu is to display list of cards as and str
            
            Example:
                >>> display_cards(['2 ♠', '9 ♣', '10 ♠','A ♠'])
                '2♠ 9♣ 10♠ A♠ '
                >>> display_cards(['2 ♥', '3 ♣', '6 ♠', '7 ♣', 'Q ♠'])
                '2♥ 3♣ 6♠ 7♣ Q♠ '
                >>> display_cards(['5 ♠', '5 ♥', '8 ♦', 'J ♠', 'Q ♣', 'A ♥'])
                '5♠ 5♥ 8♦ J♠ Q♣ A♥ '
                >>> display_cards(['A ♥', '10 ♦', '3 ♠', '5 ♥', '7 ♦', '6 ♣'])
                'A♥ 10♦ 3♠ 5♥ 7♦ 6♣ '
                >>> display_cards(['10 ♣','Q ♠', '8 ♣',])
                '10♣ Q♠ 8♣ '
        """

        assert type(lcards) is list, 'Python list expected'
        assert self.validate_hand(lcards), 'Invalid hand'

        display_str = ""
        for each_card in lcards:
            ltemp = each_card.split()
            display_str += "".join(ltemp) + ' '
        return display_str

    def calculate_hand_value(self, player_hand: list) -> int:
        """This Modu is to calculate hand value
            
            Example:
                >>> calculate_hand_value(['9 ♥', '6 ♥', '6 ♥'])
                21
                >>> calculate_hand_value(['A ♣', '5 ♦', '10 ♠', 'A ♦'])
                17
                >>> calculate_hand_value(['4 ♣', '9 ♠', '7 ♣'])
                20
                >>> calculate_hand_value(['A ♦', 'K ♠'])
                21
                >>> calculate_hand_value(['J ♠', 'Q ♣', 'A ♥'])
                21
        """

        assert type(player_hand) is list, 'Python list expected'
        assert self.validate_hand(player_hand), 'Invalid hand'

        sum_ = 0
        nA = 0
        for item in player_hand:
            rank = (item.split())[0]
            if rank == 'A':
                nA += 1
            try:
                sum_ += int(rank)
            except:
                sum_ += 10
                if rank == 'A':
                    sum_ += 1
        while nA > 0:
            if sum_ > 21:
                sum_ -= 10
            nA -= 1
        return sum_

    def must_draw_more(self, player_hand_val) -> bool:
        """This Modu is to check that do player have to draw more if hand less then 16, 
        and player choose don't to draw more, return True
            
            Example:
                >>> must_draw_more(0)
                True
                >>> must_draw_more(10)
                True
                >>> must_draw_more(15)
                True
        """

        assert type(player_hand_val) is int, 'Python int expected'

        if player_hand_val < 16:
            return True
        else:
            q = input("More cards? (Y/N): ").lower()
            if q == 'y':
                return True
            else:
                return False

    def com_must_draw_more(self, Com_hand_value, Your_hand_value) -> bool:
        """This Modu is to check that do computer have to draw more if need to this will return True, and False in otherwise
            
            Example:
                >>> com_must_draw_more(0, 0)
                True
                >>> com_must_draw_more(11, 11)
                True
                >>> com_must_draw_more(16, 10)
                False
                >>> com_must_draw_more(18, 19)
                True
                >>> com_must_draw_more(20, 19)
                False
        """

        assert ((type(Com_hand_value) is int) and (type(Your_hand_value) is int)), 'Python int expected'

        if Com_hand_value < Your_hand_value or Com_hand_value < 16:
            return True
        else:
            return False

    def check_winner(self, player_hand_value, com_hand_value, win, loose, tie):
        """This Modu is to decide the winner
        """

        for input_value in [player_hand_value, com_hand_value]:
            assert type(input_value) is int, 'Python int expected'

        if player_hand_value > com_hand_value:
            print("You win!")
            win += 1
        elif player_hand_value < com_hand_value:
            print("You loose!")
            loose += 1
        else:
            print("You tie with the computer!!")
            tie += 1
        return win, loose, tie
