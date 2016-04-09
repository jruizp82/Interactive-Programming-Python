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
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        ans = ""
        for i in self.cards:
            ans += (i.suit+i.rank+" ")
        return "Hand contains " + ans

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        hasACE = False
        for i in self.cards:
            value += VALUES[i.rank]
            if i.rank == "A":
                hasACE = True
        if hasACE and (value<=11):
            value += 10
        return value
   
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        for i in range(len(self.cards)):
            self.cards[i].draw(canvas, [pos[0] + i*80, pos[1]])
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = [Card(i,j) for i in SUITS for j in RANKS]
        
        
    def shuffle(self):
        # add cards back to deck and shuffle
        # use random.shuffle() to shuffle the deck
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()
    
    def __str__(self):
        # return a string representing the deck
        ans = ""
        for i in self.cards:
            ans += (i.suit+i.rank+" ")
        return "Deck contains " + ans



#define event handlers for buttons
def deal():
    global outcome, in_play, game_deck, play_hand, deal_hand, hand_win, score

    # your code goes here
    if in_play:
        hand_win = "Interruption! You lose!"
        outcome = "New Deal?"
        score -= 1
        in_play = False
    else:
        hand_win = " "
        game_deck = Deck()
        game_deck.shuffle()
        play_hand = Hand()
        deal_hand = Hand()
        for t in range(2):
            play_hand.add_card(game_deck.deal_card())
            deal_hand.add_card(game_deck.deal_card()) 	
        outcome = "Hit or Stand?"
        in_play = True

def hit():
    # replace with your code below
    global play_hand, game_deck, in_play, hand_win, score, outcome
    # if the hand is in play, hit the player
    if in_play:
        play_hand.add_card(game_deck.deal_card())
        
    # if busted, assign a message to outcome, update in_play and score
        if play_hand.get_value() > 21:
            in_play = False
            hand_win = "You are busted!"
            outcome = "New Deal?"
            score -= 1
       
def stand():
    # replace with your code below
    global outcome, in_play, game_deck, deal_hand, hand_win, score
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        in_play = False
        while deal_hand.get_value() < 17:
            deal_hand.add_card(game_deck.deal_card())
        
        outcome = "New Deal?"
        if deal_hand.get_value() > 21:
            hand_win = "Dealer busted! You win!"
            score += 1
        elif deal_hand.get_value() >= play_hand.get_value():
            hand_win = "Dealer wins!"
            score -= 1
        else:
            hand_win = "Player wins!"
            score += 1

    
 
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text("Blackjack", (220, 50), 40, "Red", "sans-serif")   
    canvas.draw_text("Player ("+str(play_hand.get_value())+")", (60, 370), 25, "Black")
    canvas.draw_text(hand_win, (300, 170), 25, "Black")
    canvas.draw_text(outcome, (300, 370), 25, "Black")
    canvas.draw_text("Score: "+str(score), (400, 120), 25, "Fuchsia")
    deal_hand.draw(canvas, [20, 200])
    play_hand.draw(canvas, [20, 400])
    if in_play:
        canvas.draw_text("Dealer", (60, 170), 25, "Black")
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [56.5, 249], CARD_BACK_SIZE)
    else:
        canvas.draw_text("Dealer ("+str(deal_hand.get_value())+")", (60, 170), 25, "Black")

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