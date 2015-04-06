#http://www.codeskulptor.org/#user39_REsp4sGqtx_14.py

# Mini-project #6 - Blackjack

import simplegui
import random
CANVAS_WIDTH = 600
CANVAS_HEIGHT = 600
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

game_status = ""

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
        self.hand=[]	# create Hand object

    def __str__(self):
        hand_str="Hand Contains:"
        for dummy_card in self.hand:
            hand_str=hand_str+" "+str(dummy_card)	# return a string representation of a hand
        hand_str += " Score:"+str(self.get_value())
        return hand_str
    def __len__(self):
        return len(self.hand)
    
    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        score=0
        for dummy_card in self.hand:
            score=score+VALUES[dummy_card.get_rank()]
        for dummy_card in self.hand:
            if dummy_card.get_rank()=='A'\
            and score+10<21:
                score+10
        return score
   
    def draw(self, canvas, pos):
        for dummy_card in self.hand:
            dummy_card.draw(canvas, pos)
            pos[0]+=CARD_SIZE[0]
            # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck=[]
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
            

    def shuffle(self):
       random.shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()	# deal a card object from the deck
    
    def __str__(self):
        deck_str="Deck Contains:"+str(len(self.deck))\
        + " cards \n"
        for dum_card in self.deck:
            deck_str += " " + str(dum_car)
        return deck_str

#Initializes score and wager variables
def score_init():
    global wager,play_score,deal_score
    
    play_score=0
    deal_score=0
    wager=10
    
def wage_inp(input):
    global wager
    if in_play==False:
        try:
            wager=int(input)
        except:
            wager=10
        
def player_wins():
    global wager,play_score,deal_score,in_play,game_status
    game_status="Player wins!! New Deal?"
    play_score += wager
    deal_score -= wager
    in_play = False
    
def dealer_wins():
    global wager,play_score,deal_score,in_play,game_status
    game_status="Player loses!! New Deal?"
    play_score -= wager
    deal_score += wager
    in_play = False
    
def deal():
    global outcome, in_play
    global new_deck,hand_play,hand_deal
    global game_status
    
    if in_play == True:
        dealer_wins()
    else:
        new_deck=Deck()
        new_deck.shuffle()
        hand_play=Hand()
        hand_deal=Hand()

        for cards in range(2):
            hand_play.add_card(new_deck.deal_card())
            hand_deal.add_card(new_deck.deal_card())


        in_play = True

        game_status="Hit or Stand?"

#Deals card to player when pressed
#Busts player if score goes over 21
def hit():
    global in_play,game_status
    if in_play == True:
        hand_play.add_card(new_deck.deal_card())
        if hand_play.get_value()>21:
            dealer_wins()
    
#Deals card to dealer till score of 17 or more
#Calculates game result
def stand():
    global in_play,game_status
    if in_play == True:
        while hand_deal.get_value()<=17:
            hand_deal.add_card(new_deck.deal_card())
    
        if hand_deal.get_value()>21:
            player_wins()
        elif hand_play.get_value()>hand_deal.get_value:
            player_wins()
        else:
            dealer_wins()
            

# draw handler    
#handles drawing of objects on canvas
def draw(canvas):
     #variables to link text positions to canvas
    #width and height
    deal_vert=0.25
    player_vert=0.75
    message_vert=0.6
    cards_hor=0.3
    
    #variables to control draw positions of cards
    hor_card_start=CANVAS_WIDTH*cards_hor
    ver_player_start=CANVAS_HEIGHT*player_vert
    ver_dealer_start=CANVAS_HEIGHT*deal_vert
    
    #Draw game title
    canvas.draw_text("Welcome to Blackjack-Lite",(CANVAS_WIDTH*0.1,
                                  CANVAS_HEIGHT*.1),
                     45,'Black')
   
    #Draw game status
    canvas.draw_text(game_status,(CANVAS_WIDTH*0.3,
                                  CANVAS_HEIGHT*message_vert),
                     40,'Fuchsia')
   
    
    #draw player hand
    
    hand_play.draw(canvas,[hor_card_start,ver_player_start])
    
    #draw dealer hand
    
    hand_deal.draw(canvas,[hor_card_start,ver_dealer_start])
    
    #keep dealer hole card covered during game
    if in_play == True:
        canvas.draw_text("Dealer Cards",(CANVAS_WIDTH*0.1,
                                  ver_dealer_start-30),
                     30,'Red')
        canvas.draw_text("Player Cards",(CANVAS_WIDTH*0.1,
                                  ver_player_start-30),
                     30,'Blue')
        canvas.draw_image(card_back,\
                          CARD_BACK_CENTER,CARD_BACK_SIZE,
                          (hor_card_start+CARD_BACK_CENTER[0],
                           ver_dealer_start+CARD_BACK_CENTER[1]),
                          CARD_BACK_SIZE)
    else:
        #show hand scores at end of round
        deal_hand="Dealer Hand: "+ str(hand_deal.get_value())
        canvas.draw_text(deal_hand,(CANVAS_WIDTH*0.3,
                                  CANVAS_HEIGHT*(message_vert+0.05)),
                     30,'Red')
        play_hand="Player Hand: "+ str(hand_play.get_value())
        canvas.draw_text(play_hand,(CANVAS_WIDTH*0.3,
                                  CANVAS_HEIGHT*(message_vert+0.1)),
                     30,'Blue')
    
    label_player.set_text("Player Score: "+str(play_score))
    label_dealer.set_text("Dealer Score:"+str(deal_score))
    label_wager.set_text("Current Wager: "+str(wager))
# initialization frame
frame = simplegui.create_frame("Blackjack", CANVAS_WIDTH,\
                               CANVAS_HEIGHT)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)

frame.add_label("")
label_player=frame.add_label("Player Score: 0")
label_dealer=frame.add_label("Dealer Score: 0")
frame.add_label("")
label_wager=frame.add_label("Current Wager: 10")
wage_inp_handle=frame.add_input('Set Wager',wage_inp, 50)

frame.set_draw_handler(draw)


# get things rolling
deal()
score_init()
frame.start()


