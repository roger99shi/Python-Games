# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        self.show=True
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        if self.show:
            card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE,
                              (pos[0] + CARD_BACK_CENTER[0],
                               pos[1] + CARD_BACK_CENTER[1]),
                              CARD_BACK_SIZE)

            
# define hand class
class Hand:
    def __init__(self):
        self.hand=[]	# create Hand object

    def __str__(self):
        return "Hand contains "+" ".join([str(card) for card in self.hand])
    
    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        value=0
        aces =0
        for card in self.hand:
            value+=VALUES.get(card.get_rank())
            if card.get_rank()=="A":
                aces+=1
        if value+10*aces<=21:
            value=value+10*aces
        return value
            # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        i = 0
        for card in self.hand:
            card.draw(canvas, (pos[0] + (30 * i), pos[1]))
            i += 1	# draw a hand on the canvas, use the draw method for cards

 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))# create a Deck object

    def shuffle(self):
        random.shuffle(self.deck)
        # shuffle the deck 
            # use random.shuffle()

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        return "Deck contains "+" ".join([str(card) for card in self.deck])
    


#define event handlers for buttons
def deal():
    global outcome, in_play, deck,player,dealer, score 
    if in_play:
        score -=1
    deck=Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    outcome ="Hit or Stand?"
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.hand[-1].show = False
    in_play = True
    print player
    print dealer

    # your code goes here
    
    in_play = True

def hit():
    global outcome,in_play,score
    if player.get_value()>21:
        outcome= "You have busted"
        in_play = False
        score -=1
    else:
        player.add_card(deck.deal_card())# replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome,in_play,score
    dealer.hand[-1].show = True
    if player.get_value()>21:
        outcome= "You have busted"
        in_play = False
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
            if dealer.get_value()>21:
                outcome= "You win!"
                score+=1
            elif player.get_value() > dealer.get_value():
                outcome= "You win!"
                score+=1
            else:
                outcome= "You lose."
                score-=1
            in_play= False# replace with your code below
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text(outcome, (300, 300), 18, "White")
    canvas.draw_text(str(score), (150, 300), 18, "White")
    player.draw(canvas, [40, 400])
    
    dealer.draw(canvas, [40, 50])
        



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric