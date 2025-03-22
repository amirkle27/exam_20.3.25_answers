import enum
from encodings.punycode import selective_find


class CardSuit(enum.Enum):

    CLUBS = 1
    DIAMONDS = 2
    HEARTS = 3
    SPADES = 4

    def __eq__(self, other):
        if isinstance(other, CardSuit):
            return self.value == other.value

    def __lt__(self, other):
        if isinstance(other,CardSuit):
            return self.value < other.value

    def __gt__(self, other):
        if isinstance(other,CardSuit):
            return self.value > other.value

    def __hash__(self):
        return hash(self.value)

class CardRank(enum.Enum):

    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13
    ACE = 14

    def __eq__(self, other):
        if isinstance(other,CardRank):
            return self.value == other.value

    def __hash__(self):
        return hash(self.value)

    def __lt__(self, other):
        if isinstance(other,CardRank):
            return self.value < other.value

    def __gt__(self, other):
        if isinstance(other,CardRank):
            return self.value > other.value

class Card:
    def __init__(self, suit:CardSuit, rank:CardRank, face_up:bool = True):
        self._suit = suit
        self._rank = rank
        self._face_up = face_up

    def __eq__(self, other):
        if isinstance(other, Card):
            return self._rank == other._rank and self._suit == other._suit

    def __lt__(self, other):
        if isinstance(other, Card):
            if self._rank == other._rank:
                return self._suit < other._suit
            return self._rank < other._rank

    def __gt__(self, other):
        if isinstance(other,Card):
            if self._rank == other._rank:
                return self._suit > other._suit
            return self._rank > other._rank

    def __hash__(self):
        return hash((self._suit, self._rank))

    def __str__(self):
        if self._face_up:
            return self.get_display_name()
        return "?"

    def __repr__(self):
        return (f"Card(suit = {self._suit}, rank = {self._rank}, face_up = True)")

    @property
    def suit(self):
        return self._suit.name

    @property
    def rank(self):
        return self._rank.name

    @property
    def face_up(self):
        return self._face_up

    def flip(self):
        if self._face_up:
            self._face_up = False
        else:
            self._face_up = True

    def get_display_name(self):
        return f"{self._rank.name} of {self._suit.name} "

class Deck:
    def __init__(self):
        self._cards = []
        self._index = iter


TWO = CardRank(CardRank.TWO)
THREE = CardRank(CardRank.THREE)

#

# print(four.face_up)
# four.flip()
# print(four.face_up)
# four.flip()
# print(four.face_up)
# print(four.suit)
# print(four.rank)
# print(four.get_display_name())
#
#
# def __eq__(self, other):
#     if isinstance(other, Card):
#         return self._rank == other._rank and self._suit == other._suit
#
# def __lt__(self, other):
#     if isinstance(other, Card):
#         if not self._rank == other._rank:
#             return self._rank < other._rank
#         else:
#             return self._suit < other._suit

four = Card(CardSuit.CLUBS, CardRank.FIVE)
fourr = Card(CardSuit.DIAMONDS,CardRank.FIVE)

print(four.suit)
print(fourr.suit)
print(four<fourr)
print(hash(four))
print(four)
four.flip()
print(four)
print(repr(four))