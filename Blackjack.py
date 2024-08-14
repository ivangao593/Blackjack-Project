import random

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
        self.hand_value = 0
        self.stand = False
        self.win = False
        self.bust = False
    
    def hit(self):
        card = random.choice(deck)
        self.hand.append(card)
        deck.remove(card)
    
    def update_value(self):
        self.hand_value = 0
        ace_count = 0
        for c in self.hand:
            v = c.split(" ")
            if v[0] == "Ace":
                ace_count += 1
            elif v[0] == "Jack" or v[0] == "Queen" or v[0] == "King":
                self.hand_value += 10
            else:
                self.hand_value += int(v[0])
        for a in range(ace_count):
            if self.hand_value + 11 > 21:
                    self.hand_value += 1
            else:
                self.hand_value += 11

    def show_hand(self):
        return self.hand

# Welcome
print("Welcome to Blackjack!")
print("--------------------")

# Creating players
num_players = int(input("How many players? "))

while num_players < 1 or num_players > 4:
    print("Not a valid number. Choose 1-4.")
    num_players = int(input("How many players? "))

print("--------------------")

pList = []

dealer = Player("Dealer")

p1Name = input("Player 1 Name: ")
p1 = Player(p1Name)
pList.append(p1)

if num_players > 1:
    p2Name = input("Player 2 Name: ")
    p2 = Player(p2Name)
    pList.append(p2)

if num_players > 2:
    p3Name = input("Player 3 Name: ")
    p3 = Player(p3Name)
    pList.append(p3)

if num_players > 3:
    p4Name = input("Player 4 Name: ")
    p4 = Player(p4Name)
    pList.append(p4)

print("--------------------")

# Starting game
print("Dealing Cards...")

dealer.hit()
dealer.hit()
dealer.update_value()
dealer_public = [dealer.hand[0], "Mystery Card"]
print(dealer.name + "'s Hand: " + str(dealer_public))

for player in pList:
    player.hit()
    player.hit()
    player.update_value()
    print(player.name + "'s Hand: ", end="")
    print(player.show_hand(), end="")
    print(" Hand Value = " + str(player.hand_value))

print("--------------------")

# Continuing play
standed_players = []
winning_players = []
losing_players = []
tie_players = []

for player in pList:
    while player.stand == False and player.win == False and player.bust == False:
        print(player.name + "'s Hand: ", end="")
        print(player.show_hand())
        print("Hand Value: " + str(player.hand_value))
        if player.hand_value == 21:
            player.win = True
            winning_players.append(player)
            print(player.name + " has won")
            continue
        choice = input(player.name + ": Hit / Stand\n")
        if choice == "Stand":
            player.stand = True
            standed_players.append(player)
        if choice == "Hit":
            player.hit()
            player.update_value()
            print(player.name + "'s Hand: ", end="")
            print(player.show_hand())
            print("Hand Value: " + str(player.hand_value))
            if player.hand_value == 21:
                player.win = True
                winning_players.append(player)
                print(player.name + " has won")
            if player.hand_value > 21:
                player.bust = True
                losing_players.append(player)
                print(player.name + " has busted")
        print("--------------------")

# Dealer's turn
if len(standed_players) != 0:
    print("Dealer's Turn")
    print(dealer.name + "'s Hand: ", end = "")
    print(dealer.show_hand())
    print("Hand Value: " + str(dealer.hand_value))
    while dealer.hand_value <= 16:
        print("Dealer Hits")
        dealer.hit()
        dealer.update_value()
        print(dealer.name + "'s Hand: ", end = "")
        print(dealer.show_hand(), end="")
        print(" Hand Value = " + str(dealer.hand_value))
        if dealer.hand_value == 21:
            print("Dealer has won")
            for p in standed_players:
                if p.hand_value < 21:
                    losing_players.append(p)
                else:
                    tie_players.append(p)
        if dealer.hand_value > 21:
            print("Dealer has busted")
            for p in standed_players:
                winning_players.append(p)

    # Comparing cards
if dealer.hand_value < 21:
    for p in standed_players:
        if p.hand_value < dealer.hand_value:
            losing_players.append(p)
        elif p.hand_value == dealer.hand_value:
            tie_players.append(p)
        else:
            winning_players.append(p)

# Standings
print("--------------------")
print(dealer.name + "'s Hand: ", end = "")
print(dealer.show_hand(), end="")
print(" Hand Value = " + str(dealer.hand_value))
for p in pList:
    print(p.name + "'s Hand: ", end="")
    print(p.show_hand(), end="")
    print(" Hand Value = " + str(p.hand_value))
print("--------------------")

# Results
print("Winning Players: ")
for p in winning_players:
    print(p.name)
print("--------------------")
print("Losing Players: ")
for p in losing_players:
    print(p.name)
print("--------------------")
print("Tied Players: ")
for p in tie_players:
    print(p.name)