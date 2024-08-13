# Creating the deck
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
deck = []
for r in ranks:
    for s in suits:
        deck.append(r + " of " + s)

# Defining a player
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self):
        return self.hand

# Starting game
print("Welcome to Blackjack!")

# Number of players
num_players = int(input("How many players? "))
while num_players < 1 or num_players > 4:
    print("Not a valid number. Choose 1-4.")
    num_players = int(input("How many players? "))


