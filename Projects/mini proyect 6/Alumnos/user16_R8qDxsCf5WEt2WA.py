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
        # create Hand object
        self.value = 0	
        self.nbr_of_cards = 0
        self.cards = []

     def __str__(self):
        # return a string representation of a hand
        string="Hand contains "
        for i in range(self.nbr_of_cards):
            string = string + self.cards[i].get_suit() + self.cards[i].get_rank() + " "
        return string

     def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)
        self.nbr_of_cards += 1

     def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        nbr_aces = 0
        for i in range(self.nbr_of_cards):
            cur_rank=self.cards[i].get_rank()
            if cur_rank == 'A':
                nbr_aces += 1
            value += VALUES[cur_rank]
        
        if (nbr_aces >= 1) and (value + 10) <= 21:
            value += 10
        
        return value
           
   
     def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        position = pos
        for i in range(self.nbr_of_cards):
            self.cards[i].draw(canvas, position)
            position[0] = pos[0] + CARD_SIZE[0] + 10
            
 
        
# define deck class 
class Deck:
    def __init__(self):	
        self.cards=[]
        self.nbr_of_cards = 0
        for i in SUITS:
            for j in RANKS:
                currentcard=Card(i,j)
                self.cards.append(currentcard)
                self.nbr_of_cards += 1             
        
    def __str__(self):
        # return a string representation of a deck
        string="Deck contains "
        for i in range(self.nbr_of_cards):
            string = string + self.cards[i].get_suit() + self.cards[i].get_rank() + " "
        return string

    def deal_card(self):
        self.nbr_of_cards -= 1
        return self.cards.pop()
    
    def shuffle(self):
        random.shuffle(self.cards)

the_deck=Deck()
player_hand=Hand()
dealer_hand=Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play, the_deck, player_hand, dealer_hand, score
    # your code goes here
    if in_play == False:
        the_deck=Deck()
        player_hand=Hand()
        dealer_hand=Hand()
        the_deck.shuffle()
        player_hand.add_card(the_deck.deal_card())
        dealer_hand.add_card(the_deck.deal_card())
        player_hand.add_card(the_deck.deal_card())
        dealer_hand.add_card(the_deck.deal_card())
        outcome=""
        in_play = True
    else:
        outcome = "You loose the game"
        score -= 1
        in_play = False

    
def hit():
    global outcome, in_play, score
    # if the hand is in play, hit the player
    if in_play == True:
        if player_hand.get_value() <= 21:
            player_hand.add_card(the_deck.deal_card())
            # if busted, assign a message to outcome, update in_play and score
            if player_hand.get_value() > 21:
                outcome = "You went busted and loose"
                in_play = False
                score -= 1
                   
def stand():
    global in_play, outcome, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:
        while dealer_hand.get_value() <= 17:
           dealer_hand.add_card(the_deck.deal_card())
        
        # assign a message to outcome, update in_play and score            
        if (player_hand.get_value() <= dealer_hand.get_value()) and (dealer_hand.get_value() <= 21) or (player_hand.get_value() > 21):
            outcome = "You loose"
            score -= 1
        else:
            outcome = "You won"
            score += 1
        
    in_play = False


# draw handler    
def draw(canvas):
    canvas.draw_text("Blackjack", (250, 50), 25, "Black")  
    canvas.draw_text("Player:", (50, 140), 20, "Black") 
    canvas.draw_text("Dealer:", (50, 390), 20, "Black") 
    canvas.draw_text(outcome, (100, 100), 20, "Red")
    canvas.draw_text("score : " + str(score), (450, 100), 20, "Black")
    player_hand.draw(canvas,[50, 150])
    dealer_hand.draw(canvas,[50, 400])
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50+CARD_BACK_CENTER[0],400+CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
        canvas.draw_text("Hit or Stand ? ", (250, 550), 20, "Blue")
    else:
        canvas.draw_text("New Deal ? ", (250, 550), 20, "Blue")
    


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
deal()


# remember to review the gradic rubric