#!python

import collections

Card = collections.namedtuple("Card", ["rank", "suit"])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    suits = "spades diamonds clubs hearts".split()

    def __init__(self) -> None:
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


beer_card = Card("7", "diamonds")
print(f"{beer_card = }\n")

deck = FrenchDeck()
print(f"{len(deck) = }\n")
print(f"{deck[0] = }\n")
print(f"{deck[-1] = }\n")

from random import choice

print(f"{choice(deck) = }\n")
print(f"{choice(deck) = }\n")
print(f"{choice(deck) = }\n")

print(f"{deck[:3] = }\n")
print(f"{deck[12::13] = }\n")

for card in deck:
    print(f"{card = }\n")

for card in reversed(deck):
    print(f"{card = }\n")

print(f"{Card('Q', 'hearts') in deck = }\n")
print(f"{Card('7', 'beasts') in deck = }\n")


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(f"{card = }\n")
