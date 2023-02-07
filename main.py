import random
from random import shuffle

class card:
    suits = ["Spades", "Diamonds", "Hearts", "Clubs"]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    def __init__(self, v, s):
        self.value = v
        self.suit = s

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(card(i, j))

        shuffle(self.cards)
        
    def rm_card(self):
        print(len(self.cards))
        if len(self.cards) == 0:
            return
        else:
            return self.cards.pop()
    
class Player:
    def __init__(self, name):
        self.wins = 0
        self.cards = None
        self.name = None
        self.name = name

class Game:
    def __init__(self):
        p1 = input("Enter 1st Players Name: ")
        p2 = input("Enter 2nd Players Name: ")
        self.deck = Deck()
        self.player1 = Player(p1)
        self.player2 = Player(p2)
    def play_game(self):
        cards = self.deck.cards
        while len(cards) > 2:
            q = "Q to quit or Press any key to play"
            key = input(q)
            if key.lower() == "q":
                break
            else:
                p1card = self.deck.rm_card().value
                p2card = self.deck.rm_card().value
                self.draw(self.player1.name,self.player2.name, p1card, p2card)
                if p1card > p2card:
                    self.player1.wins += 1
                    self.win(self.player1.name)
                elif p1card < p2card:
                    self.player2.wins += 1
                    self.win(self.player2.name)
        result = self.winner(self.player1, self.player2)
        print(result)

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        elif p2.wins > p1.wins:
            return p2.name
        elif p1.wins == p2.wins:
            return("Its a tie")

    def draw(self, p1name, p2name, p1card, p2card):
        print(p1name, " drew ", p1card)
        print(p2name, " drew ", p2card)

    def win(self, winner):
        print(winner, " won the game.")

game = Game()
game.play_game()