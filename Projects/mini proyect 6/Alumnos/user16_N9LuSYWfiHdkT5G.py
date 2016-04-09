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
outcome = "Deal?"
font_color = "white"
player_score = 0
dealer_score = 0

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
        self.hand_cards=[]	

    def __str__(self):
        hand_str = "Hand contains: "
        if len(self.hand_cards)>0:
            for i in range(len(self.hand_cards)):
                hand_str += str(self.hand_cards[i])
                hand_str += " "
        return  hand_str
# return a string representation of a hand

    def add_card(self, card):
        self.hand_cards.append(card)

    def get_value(self):
        value=0
        aces=0
        for card in self.hand_cards:
            value+=VALUES[card.get_rank()]
            if card.get_rank() =="A":
                aces += 1
                
        if aces>=1 and value+10<=21:
            value += 10    
        return value

    def draw(self, canvas, pos):
        for card in self.hand_cards:
            card.draw(canvas,pos)
            pos[0]+=75
            
      

        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_cards=[]
        self.dealt_cards=[]
        for suit in SUITS:
            for rank in RANKS:
                card = Card(suit,rank)
                self.deck_cards.append(card)
        random.shuffle(self.deck_cards)
        random.shuffle(self.deck_cards)

    def shuffle(self):
        self.deck_cards=self.deck_cards + self.dealt_cards
        random.shuffle(self.deck_cards)
        random.shuffle(self.deck_cards)

    def deal_card(self):
        self.dealt_cards.append(self.deck_cards[-1])
        self.deck_cards.pop()
        return self.dealt_cards[-1]
        
    
    def __str__(self):
        deck_str = "Deck contains: "
        if len(self.deck_cards)>0:
            for i in range(len(self.deck_cards)):
                deck_str += str(self.deck_cards[i])
                deck_str += " "
        return  deck_str
    
    def draw(self,canvas,pos):
        if len(self.deck_cards)>0:
            canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, pos,CARD_BACK_SIZE)
        else:
            canvas.draw_text("empty deck",CARD_BACK_CENTER,"white")

#define event handlers for buttons
def deal():
    global player_hand,bj_deck, dealer_hand
    global outcome, in_play, font_color, dealer, dealer_score
   
    if not in_play:
        bj_deck = Deck()
        bj_deck.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        
        dealer_hand.add_card(bj_deck.deal_card())
        player_hand.add_card(bj_deck.deal_card())
        dealer_hand.add_card(bj_deck.deal_card())
        player_hand.add_card(bj_deck.deal_card())
        in_play = True
        outcome="Hit or Stand?"
        font_color="white"
        dealer=True
    else:
        in_play = False
        outcome="You loose. Want another deal?"
        dealer_score += 1

    
    
    

def hit():
    global in_play,outcome,player_score,dealer_score,font_color,dealer
    if player_hand.get_value()+dealer_hand.get_value()>0:
        if in_play:
            if player_hand.get_value()<=21:
               player_hand.add_card(bj_deck.deal_card())
               if player_hand.get_value()>21:
                    outcome="You busted"
                    font_color="Red"
                    dealer_score += 1
                    in_play=False
                    dealer=False
            
        else:
            if dealer:
                while dealer_hand.get_value()<17:
                    dealer_hand.add_card(bj_deck.deal_card())
                if dealer_hand.get_value()>21:
                    outcome="Dealer busted. You win"
                    font_color="Red"
                    player_score += 1
                    dealer=False
                
                elif player_hand.get_value()-dealer_hand.get_value()>0:
                    outcome="You win"
                    font_color="Red"
                    player_score += 1
                    dealer=False
                
                
                else:
                    outcome="Dealer wins"
                    font_color="Red"
                    dealer_score += 1
                    dealer=False
            else:
                outcome="Hand is over. Deal again"
                font_color="Orange"
                
            
            
    
       
def stand():
    global in_play, dealer
    if player_hand.get_value()>21:
        outcome="You busted"
        font_color="Red"
        in_play=False
    else:
        in_play = False
        hit()
        
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text(outcome,[100,300],20,font_color)
    canvas.draw_text("BLACKJACK",[300,75],40,"white")
    canvas.draw_text("Dealer= "+str(dealer_score),[400,275],20,"white")
    canvas.draw_text("Player= "+str(player_score),[400,325],20,"white")
    if in_play:
        bj_deck.draw(canvas,[75,75])
        player_hand.draw(canvas,[50,400])
        dealer_hand.draw(canvas,[150,100])
        bj_deck.draw(canvas,[186,150])
        
        
    else:
        bj_deck.draw(canvas,[75,75])
        player_hand.draw(canvas,[50,400])
        dealer_hand.draw(canvas,[150,100])
        

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
player_hand = Hand()
dealer_hand = Hand()
bj_deck = Deck()


# remember to review the gradic rubric