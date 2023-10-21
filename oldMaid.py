import constant as c
import pygame
from toscards.base_cards import Card, Deck, Player, suits, values
from time import sleep
import random
import os


# old maid
def set_player_amount():
    player_limit = 11
    player_amount = int(input("how many players:\n"))
    splayer_limit = str(player_amount)
    if player_amount >= player_limit:
        print("lol imagine having " + splayer_limit + " friends, couldn't be me")
        exit()
    if player_amount == 1:
        print("Youre the old maid")
        exit()
    if player_amount == 0:
        print("This isn't a game, what are you doing with your life?")
        exit()
    if player_amount == 4:
        print("play mario games do you?")
    return player_amount


# impent into gameplay  
class OldMaidPlayer:

    def __init__(self,id,deck):
        self.id = id
        self.deck = deck
        self.player = Player(id,deck) #
        self.sort_hand()
        #for i in self.omdeck.deck.cards:
            #print(i.value)
    
    # put a card into correct location into a players hand
    # uses a linear search to find the placement for the card
    #   going from lowest to highest index cards in deck
    #       compare each card in deck against new card
    #           if values match, then insert new card after matching card
    #           if values don't match, then appened new card to deck

    def place_card_in_hand(self,new_card):
        print("pcih start - deck len:",len(self.deck.cards))
        for i in range(0, len(self.deck.cards)):
            # Match case, place new card adjecent to matching card
            if self.deck.cards[i].value == new_card.value:
                print("pcih match found")
                self.deck.cards.insert(i+1,new_card)
                return
        
        # no match found, place new card at the end of deck
        print("pcih no match found")
        self.deck.cards.append(new_card)

        print("pcih end - deck len:",len(self.deck.cards))
        return
    
    def to_string(self):
        s = ""
        for i in self.deck.cards:
            s = s + i.to_string() + '\n'
        return s 
    
    # Player discards card pairs from their hands
    #    Do linear search
    #       takes current index, i , and subtracts it at 1
    #           if* card at index i is equal to i - 1, then the cards are pair, * = it probably gonna be while statement
    #               remove and place pair into temp deck
    #           
    def play_pairs(self):   
        pairs = Deck("red",True)
        i = 1
        while i < len(self.deck.cards): 
            if self.deck.cards[i].value == self.deck.cards[i-1].value:
                #print("I:", i, "I-1:", i-1, self.deck.cards[i].value,self.deck.cards[i-1].value)
                c = self.deck.cards.pop(i)
                pairs.cards.append(c)
                c = self.deck.cards.pop(i-1)
                pairs.cards.append(c)
                #print(pairs.size())
                continue
            i += 1
            
        return pairs


    def sort_hand(self):
        #for i in self.deck.cards:
            #print(i.value)
        self.deck.cards.sort(key=lambda card: card.value) # TODO figure out lambda
        #for i in self.deck.cards:
            #print(i.value)
    
    def get_card(self, index):
        return self.deck.cards.pop(index)
    
    def card_count(self):
        return self.deck.size()
    
    def get_id(self):
        return self.id

"""
td = Deck("bluga",False)
tp = OldMaidPlayer("test",td)
tp.sort_hand()
nc = Card("hearts","7")
tp.place_card_in_hand(nc)
#print(tp.to_string())
o = tp.play_pairs()
print(o.size())
print(td.size())
"""



class Game:
    # ranks ={"2": 2, "3" : 3,"4": 4,"5" : 5, "6": 6, "7": 7, "8": 8,"9" : 9, "10": 10, "jack": 11, "queen": 12, "king" : 13, "ace" : 14}
    
    def __init__(self):
        # sets player amount and then generates player decks.
        player_amount = set_player_amount()
        self.player_amount = player_amount
        self.deck_original = Deck("red",False)  # This is the dealers deck
        self.player_decks = []
        for i in range(self.player_amount):
            decks = Deck("red",True)
            self.player_decks.append(decks)
        print()
        
        # Deals out cards and removes the first queen
        count = 0 # is player index
        firstQueen = False
        while not self.deck_original.is_empty():
            current_deck = count % self.player_amount # Picking the next deck to put a card into
            card = self.deck_original.draw()
            if card.value == values[c.QUEENVALUE] and firstQueen == False:
                firstQueen = True
                continue
            self.player_decks[current_deck].put(card)
            count += 1
        
        # create players and inserting decks into them
        self.player_list = []
        for i in range(self.player_amount):
            players = OldMaidPlayer("player" + str(i),self.player_decks[i]) # player names maybe later
            self.player_list.append(players)
    
    def play(self):
        
        game_on = True # loop of gameplay continues until false
        g_output = "" # stores game output that will be sent to console 


        # Iterate through players
        #     Each player sorts cards by value
        j = 0
        while j in self.player_list:
            self.player_list[j].sort_hand()
            j += 1
        
        pc = 1 # Player count
        count = 0 # to control player turn

        temp_deck = Deck("red",True)
        dealer = None
        
        #  During gameplay, is modified to go counter clockwise than clockwise
        #   If players is greater than 1, remaining player is the old hag
        #     For each player in order:
        #       Put down all pairs, linear scan of deck to identify pairs and play pairs
        #       Determine if deck empty, remove player from list if empty
        #       Take card from neighbor, perform insertion sort to put card in their deck (where it belongs - TLC)
        #
        print("pl_len:", len(self.player_list))
        while len(self.player_list) > pc: # pc == 1
            current_idx = (len(self.player_list) - 1) - (count % (len(self.player_list)))
            next_player_idx = (len(self.player_list) - 1) - ((count + 1) % (len(self.player_list)))
            print("idx:",current_idx)
            current_player = self.player_list[current_idx]
            next_player = self.player_list[next_player_idx]
            current_id = current_player.get_id()
            print("pid:",current_id)
            pairs_deck = current_player.play_pairs()
            print("len pairs",pairs_deck.size())
            temp_deck.append(pairs_deck,False)
            print("TD:",temp_deck.size())
            cpd_sz = current_player.card_count()

            if cpd_sz < 2:
                print("inside 2")
                # one card then out
                if cpd_sz == 1:
                    print("inside 1")
                    # pass remaining card to player on right 
                    next_player.place_card_in_hand(current_player.get_card(0))

                    
                # out of cards
                self.player_list.pop(current_idx)
                
                # special case, removing last element must increment count
                if current_idx == len(self.player_list) - 1:
                    count += 1
                # go back to top of loop
                continue
        
                
            print("standard flow")
            # pass a card to player on right
            random_idx = random.randint(0, (cpd_sz -1))
            next_player.place_card_in_hand(current_player.get_card(random_idx))



            count += 1
        
        # print loser
        print("losing player: ",self.player_list[0].get_id())

# PYGAME

# Global variables for pygame
scaled_images ={}

# Measurements
WIDTH = 0
HEIGHT = 0


WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("War")

icon = pygame.image.load(os.path.join('icon',"castle.png"))
pygame.display.set_icon(icon)

# Colors
GREEN = (53, 101, 77)
BLUE = (0, 0, 255)



#FPS = 60

for i in suits:
    for j in values:
        cs = i + "_" + j
        card = pygame.image.load(os.path.join('/Users/tobinclouser/Documents/code/py/assets/cards',cs + ".png"))
        scaled_images[cs] = pygame.transform.scale(card,(150,250))

back = pygame.image.load(os.path.join('/Users/tobinclouser/Documents/code/py/assets/cards',"red.png"))
back_scale = pygame.transform.scale(back,(150,250))

def load_player(player):
    p = pygame.image.load(os.path.join('/Users/tobinclouser/Documents/code/py/assets/cards', player + ".png"))
    return p



g = Game()
g.play()

