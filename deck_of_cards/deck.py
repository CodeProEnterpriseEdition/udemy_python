# aloitus 8.30

from random import shuffle as shuffle_cards
# from Card import Card

class Card:

    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:

    def __init__(self):
        self.cards = []
        # self.count = 0
        self._init_deck()

    def _init_deck(self):
        suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
        # face_cards = ["A", "K", "Q", "J"]
        values = ["A", "2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.cards = [Card(value,suit) for suit in suits for value in values]
        # for suit in suits:
        #     for value in range(1,14):
        #         if value == 1:
        #             value = face_cards[0]
        #         if value == 13:
        #             value = face_cards[1]
        #         if value == 12:
        #             value = face_cards[2]
        #         if value == 11:
        #             value = face_cards[3]
        #         self.cards.append(Card(suit, value))
        #         self.count += 1

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        else:
            return shuffle_cards(self.cards)

    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def deal_card(self):
        if self.count()>0:
            return self.cards.pop()
        else:
            raise ValueError("All cards have been dealt")

    def deal_hand(self, number_of_cards):
        return self._deal(number_of_cards)

    def count(self):
        return len(self.cards)

    def _deal(self, number_of_cards):
        cards_to_deal = []
        for n in range(number_of_cards):
            if self.count() > 0:
                cards_to_deal.append(self.cards.pop())
            else:
                raise ValueError("All cards have been dealt")
        return cards_to_deal


deck = Deck()
print(deck.cards)
print(deck)
print(deck.shuffle())
print(deck.deal_hand(5))
print(deck.deal_hand(5))
print(deck.deal_hand(5))
print(deck.deal_card())
print(deck.deal_card())
print(deck.deal_card())
print(deck.count)
print(deck.deal_hand(5))
print(deck.deal_hand(5))

print(deck.deal_card().suit)
print(deck.deal_card().value)
print(deck)
