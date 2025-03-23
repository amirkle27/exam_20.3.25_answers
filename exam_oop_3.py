import enum
from random import shuffle

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
        self._cards = [(rank.name,suit.name) for rank in CardRank for suit in CardSuit]
        self._index = 0
        self.suit = CardSuit
        self.rank = CardRank

    def __len__(self):
        return  len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index < len(self._cards):
            card = self._cards[self._index]
            self._index +=1
            return card
        else:
            raise StopIteration


    @property
    def cards(self):
        return self._cards

    def shuffle(self):
        shuffle(self._cards)
        return self._cards

    def draw(self):
        self._cards.remove(self._cards[0])
        return self._cards[0]

    def add_Card(self,card):
        self._cards.append(card)



deck  = Deck()
print(deck.cards)
print(deck.draw())
print(deck.cards)
print(deck.shuffle())
