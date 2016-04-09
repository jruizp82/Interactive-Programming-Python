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
outcome = "New deal?"
score = 0

# game variables
deck = None
player = None
dealer = None

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
        self.cards = []

    def __str__(self):
        result = "Hand contains "
        for c in self.cards:
            result += c.get_suit() + c.get_rank() + " "
        
        return result

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        for c in self.cards:
            value += VALUES[c.get_rank()]

        # if the hand has an ace, then add 10 to hand value in case it doesn't bust
        for c in self.cards:
            if c.get_rank() == "A" and value <= 11:
                value += 10
                
        return value
   
    def draw(self, canvas, pos):
        i = 0
        for c in self.cards:
            c.draw(canvas, [pos[0] + i * CARD_SIZE[0], pos[1]])
            i += 1
            
         
# define deck class 
class Deck:
    cards = []
    def __init__(self):
        for s in SUITS:
            for r in RANKS:
                self.cards.append(Card(s, r))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        if len(self.cards) > 0:
            return self.cards.pop(len(self.cards) - 1)
    
    def __str__(self):
        result = "Deck contains "
        for c in self.cards:
            result += c.get_suit() + c.get_rank() + " "
        
        return result


#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer

    # create the deck
    deck = Deck()
    # shuffle the deck
    deck.shuffle()
    
    # make new hands
    # player hand
    player = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    #print "Player " + str(player)
    
    # dealer hand
    dealer = Hand()
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    #print "Dealer " + str(dealer)
    
    in_play = True
    outcome = "Hit or stand?"

def hit():
    global in_play, score, player_loss, outcome
    # if the hand is in play, hit the player
    if in_play:
        if player.get_value() <= 21:
            player.add_card(deck.deal_card())
        
        #print "Player value " + str(player.get_value())
               
        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            #print "You have busted"
            in_play = False
            score -= 1
            outcome = "You lost! New deal?"
       
def stand():
    global in_play, score, outcome
    
    if not in_play:
            return
            #print "You have busted"
        
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    else:
        while dealer.get_value() < 17:
            dealer.add_card(deck.deal_card())
        
        #print "Player value " + str(player.get_value())
        #print "Dealer value " + str(dealer.get_value())
    # assign a message to outcome, update in_play and score
        if dealer.get_value() > 21:
            #print "Dealer busted"
            outcome = "You won! New deal?"
            score += 1
        else:
            if player.get_value() <= dealer.get_value():
                #print "Dealer won"
                outcome = "You lost! New deal?"
                score -= 1
            else:
                #print "Player won"
                outcome = "You won! New deal?"
                score += 1
            
    in_play = False

# draw handler    
def draw(canvas):
    # welcome text
    canvas.draw_text("Welcome to Blackjack!", (180, 50), 25, "Yellow")
    
    # outcome status
    canvas.draw_text(outcome, (180, 100), 20, "Yellow")
    
    # ensure player object is created first
    if player != None:
        player.draw(canvas, [100, 250])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# remember to review the gradic rubric