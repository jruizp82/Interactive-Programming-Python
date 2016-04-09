# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
outcome2 = ""
score = 0
my_deck = []
player_hand = []
dealer_hand = []

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
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
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.hand = []

    def __str__(self):
        # return a string representation of a hand
        ans = ""
        for card in self.hand:
            ans += " " + str(card)
        return "Hand contains" + ans

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        has_ace = False
        for card in self.hand:
            card_rank = Card.get_rank(card)
            hand_value += VALUES[card_rank]
            if card_rank == "A":
                has_ace = True           	
        
        if has_ace:
            if(hand_value + 10 <= 21):
                hand_value = hand_value + 10
            else:
                hand_value = hand_value
        
        return hand_value
            
          
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        k = 0
        for card in self.hand:
            pos = (100 + (k * 100), pos[1])
            card.draw(canvas, pos)
            k += 1
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS: 
            for rank in RANKS:
                card = Card(suit, rank)
                self.deck.append(card)

    def shuffle(self):
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        deck_string = "Deck contains "
        for i in self.deck:
              deck_string += (str(i) + " ")            
        return deck_string 



#define event handlers for buttons
def deal():
    global outcome, outcome2, in_play, score
    global my_deck, player_hand, dealer_hand
    # your code goes here
    outcome2 = ""    
    my_deck = Deck()
    my_deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    for i in range(2):
        player_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
    if in_play == True:
        score -= 1
        outcome2 = "You lose! Don't cheat!"
    in_play = True
    outcome = "Hit or Stand?"    

def hit():
    # replace with your code below
    global my_deck, player_hand, score, in_play, outcome, outcome2
    # if the hand is in play, hit the player
    if in_play:
        player_hand.add_card(my_deck.deal_card())	
        if player_hand.get_value() > 21:            
            # if busted, assign a message to outcome, update in_play and score
            outcome2 = "You have busted"
            outcome = "New Deal?"
            in_play = False
            score -= 1             
     
def stand():
    # replace with your code below
    global in_play, score, outcome, outcome2
    global player_hand, dealer_hand, my_deck
    if in_play:
        # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(my_deck.deal_card())
        # assign a message to outcome, update in_play and score
        if dealer_hand.get_value() <=21 and player_hand.get_value() <= dealer_hand.get_value():
             outcome2 = "You lose! The dealer wins"
             score -= 1            
        else:
            outcome2 = "You win!"
            score += 1                   
        outcome = "New Deal?"
        in_play = False   

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player_hand, dealer_hand, outcome, in_play
    canvas.draw_text("Blackjack",(100, 100), 48, "Blue")
    canvas.draw_text("Score", (400, 100), 32, "Black")
    canvas.draw_text(str(score),(500, 100), 32, "Black")
    canvas.draw_text("Dealer", (80, 180), 32, "Black")
    canvas.draw_text("Player", (80, 380), 32, "Black")
    canvas.draw_text(outcome, (230, 380), 32, "Black")
    canvas.draw_text(outcome2, (230, 180), 32, "Black")
    player_hand.draw(canvas, [80, 400])
    dealer_hand.draw(canvas, [80, 200])
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [136, 249], CARD_BACK_SIZE)


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
player_hand = Hand()
dealer_hand = Hand()
deal()
frame.start()


# remember to review the gradic rubric