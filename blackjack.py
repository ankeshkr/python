
import random
suits=('Heart','Club','Diamond','Spades')
ranks=('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
          'Jack','Queen','King','Ace')
values={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,
          'Jack':10,'Queen':10,'King':10,'Ace':11}
playing =True

class Card:
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.rank + " of " + self.suit
    
class Deck:
    def __init__(self):
        self.Deck = [ ]
        for suit in suits:
            for rank in ranks:
                self.Deck.append(Card(suit,rank))
                
    def __str__(self):
        deck_comp = ' '
        for card in self.deck:
            deck_comp = deck_comp + '\n' + card.__str__()
        return "the deck has" + deck_comp    

    def shuffle(self):
        random.shuffle(self.Deck)
        
    def deal(self):
        single_card=self.Deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.card=[]
        self.value=0
        self.aces=0

    def add_card(self,card):
        self.card.append(card)
        self.value+=values[card.rank]
        if card.rank =='Ace':
           self.aces+=1
    def adjust_aces(self):
        while self.value >21 and self.aces:
            self.value-=10
            self.aces-=1
class Chips:
    def __init__(self,total=100):
        self.total=total
        self.bet=0
    def win_bet(self):
        self.total+=self.bet
    def lose_bet(self):
        self.total-=self.bet
    

def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("how many chips you would like to bet?"))
        except:
            print("Please provide integer")
        else:
            if chips.bet > chips.total:
                print('Not enough chips,you have {}'.format(chips.total))
            else:
                break

def hit(deck,hand):
    single_card=deck.deal()
    hand.add_card(single_card)
    hand.adjust_aces()

def hit_or_stand(deck,hand):
    global playing
    while True:
        x=input("enter hit or stand, h or s?")
        if x[0].lower() == 's':
           print("Player stands,Dealer's turn")
           playing = False           
        elif x[0].lower()=='h':
           hit(deck,hand)
        else:
            print("Sorry I didnt understand, please enter s or h")
            continue
        break

def show_some(player,dealer):
    print("Dealers hand:")
    print("one card hidden")
    print(dealer.card[1])
    print('\n')
    print("Players hand:")
    for card in player.card:
        print(card)

def show_all(player,dealer):
    print("Dealers hand:")
    for card in dealer.card:
        print(card)
    print('\n')
    print("Players hand:")
    for card in player.card:
        print(card)    
    


    
def player_busts(player,dealer,chips):
    print("Player busts")
    chips.lose_bet()
def player_wins(player,dealer,chips):
    print("player wins")
    chips.win_bet()
def dealer_busts(player,dealer,chips):
    print("Dealer busts")
    chips.lose_bet()
def dealer_wins(player,dealer,chips):
    print("Dealer wins")
    chips.win_bet()
def push(player,dealer,chips):
    print("Dealer and winner Tie")


while True:

    print("welcome to BlackJack")
    deck =Deck()
    deck.shuffle()
    player_hand=Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand=Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips=Chips()
    take_bet(player_chips)
    show_some(player_hand,dealer_hand)
    while playing:
        hit_or_stand(deck,player_hand)
        show_some(player_hand,dealer_hand)
        if player_hand.value >21:
            player_busts(player_hand,dealer_hand,player_chips)
            break
    if player_hand.value<=21:
        while dealer_hand.value < player_hand.value:
            hit(deck,dealer_hand)
            show_all(player_hand,dealer_hand)
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)
        else:
            push(player_hand,dealer_hand,player_chips)

    print ('player total chips at {}'.format(player_chips.total))
    new_game = input('play again? y or n')
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("thank u for playing")
        break
    
        
            
        
        
        
    

        
        
    
