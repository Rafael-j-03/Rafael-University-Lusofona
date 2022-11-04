import random

player_deck = ([1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"])
npc_deck = ([1,2,3,4,5,6,7,8,9,10,"J","Q","K","A"])

def player_cards():
    global player_deck
    random.shuffle(player_deck)
    fish_player()

def npc_cards():
    global npc_deck
    random.shuffle(npc_deck)
    fish_npc()

def fish_player():
    global player_deck
    player_deck = player_deck, player_deck[12], player_deck[13]

def fish_npc():
    global npc_deck
    npc_deck = npc_deck, npc_deck[12],npc_deck[13]

def result():
    global player_deck
    player_deck = int(player_deck.index(0)) + int(player_deck.index(1))
    print(str(player_deck))
    




player_cards()
npc_cards()
result()


