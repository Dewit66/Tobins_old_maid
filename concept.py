
from toscards.base_cards import Card, Deck, Player, suits, values
import constant as c

"""
# defines amount of players there will be and can be
playerLimit = 11
playerAmount = int(input("how many players:\n"))
if playerAmount >= playerLimit:
    print("This game does not support more than" + playerLimit + "players")
    exit() 
if playerAmount == 1:
    print("Your the old maid")
    exit()
if playerAmount == 0:
    print("This isn't a game, what are you doing with your life?")
    exit()


# creates decks
deckOriginal = Deck("red",False)
playerDecks = []
for i in range(playerAmount):
    decks = Deck("red",True)
    playerDecks.append(decks)
    
for i in range(len(playerDecks)):
    print(playerDecks[i].size())


# populates the Decks
count = 0
firstQueen = False
while not deckOriginal.is_empty():
    currentDeck = count % playerAmount # Picking the next deck to put a card into
    card = deckOriginal.draw()
    if card.value == values[c.QUEENVALUE] and firstQueen == False:
        firstQueen = True
        continue
    playerDecks[currentDeck].put(card)
    count += 1

print("Amounts in deck")
for i in range(len(playerDecks)):
    print(playerDecks[i].size())


#creates players
playerList = []
for i in range(playerAmount):
    players = Player("player" + str(i),playerDecks[i]) # player names maybe later
    playerList.append(players)

print("amount in player decks")
for i in range(len(playerList)):
    print(playerList[i].deck_size())

class TesticleDeck:
    
    def __init__(self):
        self.d = Deck("blue",False)
    
    def get_card(self):
        return self.d.draw()

test = TesticleDeck()
c1 = test.get_card()
print(c1.value)

# main test
"""

class OldMaidPlayer:

    def __init__(self,id,deck):
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
        for i in range(0, len(self.deck.cards)):
            # Match case, place new card adjecent to matching card
            if self.deck.cards[i].value == new_card.value:
                self.deck.cards.insert(i+1,new_card)
                return
        
        # no match found, place new card at the end of deck
        self.deck.cards.append(new_card)
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
        kiddy = Deck("red",True)
        print(kiddy.size())
        i = 1
        while i < len(self.deck.cards): 
            if self.deck.cards[i].value == self.deck.cards[i-1].value:
                #print("I:", i, "I-1:", i-1, self.deck.cards[i].value,self.deck.cards[i-1].value)
                c = self.deck.cards.pop(i)
                kiddy.cards.append(c)
                c = self.deck.cards.pop(i-1)
                kiddy.cards.append(c)
                print(kiddy.size())
                continue
            i += 1
            

        return kiddy


    def sort_hand(self):
        #for i in self.deck.cards:
            #print(i.value)
        self.deck.cards.sort(key=lambda card: card.value) # TODO figure out lambda
        #for i in self.deck.cards:
            #print(i.value)

td = Deck("bluga",False)
tp = OldMaidPlayer("test",td)
tp.sort_hand()
print(tp.to_string())
#nc = Card("hearts","7")
#tp.place_card_in_hand(nc)
#print(tp.to_string())
o = tp.play_pairs()
#print(tp.to_string())


# list = ['g','t','t','c','c','d','d','m','m']
#print(list)
#print(len(list))
#list.pop(1)
#print(list)
#print(list[0], list[1])
#print(len(list))
# i = 1
# while i < len(list):
#     print(list)
#     print("i:",i,list[i]," i-1:", i-1,list[i-1])
#     print("start:",len(list))
#     if list[i] == list[i-1]:
#         list.pop(i)
#         list.pop(i-1)
#         print("end:",len(list))
#         continue
#     i+=1
#     print("end:",len(list))
# print(list)
