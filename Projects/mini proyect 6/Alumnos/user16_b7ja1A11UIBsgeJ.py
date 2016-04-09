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
options = "New game?"
score = 0

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
        #pass	# create Hand object
        self.hand = []

    def __str__(self):
        #pass	# return a string representation of a hand
        salida = "Hand contains"
        for card in self.hand:
            salida += " " + str(card)
        return salida
    
    def add_card(self, card):
        #pass	# add a card object to a hand
        self.hand.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        #pass	# compute the value of the hand, see Blackjack video
        value = 0
        aces = 0
        for card in self.hand:
            rank = card.get_rank()
            value += VALUES[rank]
            if (rank == 'A'):
                aces += 1
        for i in range(aces):
            if value <= 11:
                value += 10
        return value
   
    def draw(self, canvas, pos):
        #pass	# draw a hand on the canvas, use the draw method for cards
        ind = 0
        for card in self.hand:
            card.draw(canvas, [pos[0] + ind * 1 * (CARD_SIZE[0]+5), pos[1]])
            ind += 1
 
        
# define deck class 
class Deck:
    def __init__(self):
        #pass	# create a Deck object
        self.deck = []
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.deck.append(Card(SUITS[i], RANKS[j]))

    def shuffle(self):
        # add cards back to deck and shuffle
        #pass	# use random.shuffle() to shuffle the deck
        random.shuffle(self.deck)

    def deal_card(self):
        #pass	# deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        #pass	# return a string representing the deck
        salida = "Deck contains"
        for card in self.deck:
            salida += " " + str(card)
        return salida



#define event handlers for buttons
def deal():
    global outcome, score, options, in_play, deck, player, dealer

    # your code goes here
    if in_play:
        score -= 1
        outcome = "You lose"
        opciones = "New game?"
        in_play = False
    else:
        outcome = ""
        deck = Deck()
        deck.shuffle()
        player = Hand()
        dealer = Hand()
        player.add_card(deck.deal_card())
        player.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        dealer.add_card(deck.deal_card())
        options = "Hit or stand?"
    
        #print "Dealer: " + str(dealer)
        #print "Player: " + str(player)
    
        in_play = True

def hit():
    global in_play, outcome, options, score, player
    #pass	# replace with your code below
 
    # if the hand is in play, hit the player
    if in_play:
        new = deck.deal_card()
        player.add_card(new)
        #print "hit: " + str(new), "Player: " + str(player.get_value()), str(player)
   
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
        options = "New game?"
        outcome = "You have busted"
        #print "You have busted"
        if in_play:
            score -= 1
        in_play = False
    
def stand():
    #pass	# replace with your code below
    global in_play, outcome, options, score, dealer, player
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while (dealer.get_value() < 17):
            new = deck.deal_card()
            dealer.add_card(new)
            #print "stand: " + str(new), "Dealer: " + str(dealer.get_value()), str(dealer)
    # assign a message to outcome, update in_play and score      
        if (dealer.get_value() > 21):
            #print "Dealer has busted"
            outcome = "Dealer has busted"
            score += 1
        else:
            if (player.get_value() > dealer.get_value()):
                score += 1
                outcome = "Player wins"
                #print "Player wins:", player.get_value()
            else:
                score -= 1
                outcome = "Dealer wins"
                #print "Dealer wins:", dealer.get_value()
        
    options = "New game?"
    #else:
        #if player.get_value() > 21:
            #print "You have busted"
        #elif dealer.get_value() > 21:
            #print "Dealer has busted"
        #else:
            #if (player.get_value() > dealer.get_value()):
                #print "You have won:", player.get_value()
            #else:
                #print "Dealer has won:", dealer.get_value()
    in_play = False
    
    
# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    global player, dealer, outcome, options, in_play
    dealer.draw(canvas, [100, 150])
    if in_play:
        canvas.draw_image(card_back, (35.5, 48), (71, 96), (100+36.5, 150+49), (73, 98))
        canvas.draw_text("Dealer", [75, 125], 24, "Black")
    else:
        canvas.draw_text("Dealer: " + str(dealer.get_value()), [75, 125], 24, "Black")
    canvas.draw_text("Player: " + str(player.get_value()), [75, 450], 24, "Black")
    player.draw(canvas, [100, 475])
    canvas.draw_text("Blackjack", [150, 65], 64, "White")
    canvas.draw_text(options, [100, 350], 48, "Yellow") 
    canvas.draw_text(outcome, [200, 450], 48, "Blue")
    canvas.draw_text("Score: " + str(score), [475, 50], 24, "Cyan")

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deck = Deck()
player = Hand()
dealer = Hand()
frame.start()


# remember to review the gradic rubric