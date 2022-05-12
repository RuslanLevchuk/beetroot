from random import shuffle
from random import randint
cards = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
suits = ['♥', '♦', '♣', '♠']


class Card:
    def __init__(self, nominal, suite):
        self.nominal = nominal
        self.suite = suite

    def __str__(self):
        return f"[{self.nominal}|{self.suite}]"

    def show(self):
        return self.suite, self.nominal






class Deck:
    def __init__(self):
        self.deck = []
        self.set_deck()

    def set_deck(self):
        for card in cards:
            for suit in suits:
                self.deck.append(Card(card, suit))

    def deck_shuffle(self):
        shuffle(self.deck)

    def give_card(self):
        return self.deck.pop(randint(0, len(self.deck)-1))

    def __len__(self):
        #cards remainder
        return len(self.deck)

d = Deck()
for f in d.deck:
    print(f, end=' ')
print('')
d.deck_shuffle()
for f in d.deck:
    print(f, end=' ')
print('')
print(len(d))
print(d.give_card())
for f in d.deck:
    print(f, end=' ')
print('')

print(len(d))