"""
Створено функцію,яка генерує колоду карт у вигляді словника при викликанні її вперше і повертає цей словник
і умовне значення None, про шо можна вважати, що функція викликана впеше
Потім ця функція приймає цей же словник карт і при кожному виклику витягує якусь карту з колоди, модифікує словник так,
щоб цієї карти там не ставало і повертає знову модифікований словник карт і карту, яку витягнуто у вигляді списка
[карта, масть]

Ниже написав скрипт, де ми отримуємо карту, додаємо її у список відкрити карт і далі продовжуємо інтерактивно
витягувати карту

Коли колода закінчується, цей момент не опрацював, тому хай буде так, думаю, достатньо цього))
"""
import random
def paying_cards(card_remains=0):
    cards = ['6', '7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
    suits = ['♥', '♦', '♣', '♠']
    if card_remains == 0:
        deck_of_cards = {}
        for card in cards:
            deck_of_cards[card] = []
            for suit in suits:
                deck_of_cards[card].append(suit)
        return deck_of_cards, None
    else:
        deck_of_cards = card_remains
        card_choice = random.choice(list(deck_of_cards.keys()))
        suit_choice = random.choice(deck_of_cards[card_choice])
        deck_of_cards[card_choice].remove(suit_choice)
        if len(deck_of_cards[card_choice]) == 0:
            del deck_of_cards[card_choice]
        return deck_of_cards, [card_choice, suit_choice]


deck, card = paying_cards()
your_cards = {}
while True:
    inp = input('Press ENTER to get card!')
    if inp == '':
        deck, card = paying_cards(deck)
        print(f"You got: {(' '.join(i for i in card))}")
        if card[0] in your_cards.keys():
            your_cards[card[0]].append(card[1])
        else:
            your_cards[card[0]] = []
            your_cards[card[0]].append(card[1])
        if len(your_cards) == 0:
            pass
        else:
            print('Your cards:')
            for item, vals in your_cards.items():
                print(f'{item}: {" ".join(i for i in vals)}')
