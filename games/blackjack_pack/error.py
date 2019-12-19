class Error(Exception):
    """Base class for other exceptions"""
    pass


class InvalidCardRank(Error):
    """Raised when the input card rank is not a valid rank"""
    pass


class InvalidCardSuit(Error):
    """Raised when the input card suit is not a valid suit"""
    pass


class InvalidCardIndex(Error):
    """Raised when the input number of card is out of deck"""
    pass
