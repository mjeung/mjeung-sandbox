#!/usr/bin/python

from random import shuffle;
import time

#############################################################################

class ICard:
  """Base class for all Love Letter cards"""

  value = 0
  quantity = 0
  needs_target = False
  self_target_ok = False

  def name(self):
    raise NotImplementedError

  def name_value(self):
     return self.name() + "[" + str(self.value)+ "]"

  def short_description(self):
    raise NotImplementedError

  def summary(self):
    return str(self.value) + " - " + self.name() + \
             " (" + str(self.quantity) + "): " + \
             self.short_description()

#############################################################################

class PrincessCard(ICard):

   value = 8
   quantity = 1
   needs_target = False
   self_target_ok = False

   def name(self):
     return "Princess"
 
   def short_description(self):
     return "Lose if discarded"     

#############################################################################

class CountessCard(ICard):

   value = 7;
   quantity = 1;
   needs_target = False
   self_target_ok = False

   def name(self):
     return "Countess"
 
   def short_description(self):
     return "Discard if caught with King or Prince"     

#############################################################################

class KingCard(ICard):

   value = 6;
   quantity = 1;
   needs_target = True
   self_target_ok = False

   def name(self):
     return "King"
 
   def short_description(self):
     return "Trade hands"     

#############################################################################

class PrinceCard(ICard):

   value = 5;
   quantity = 2;
   needs_target = True
   self_target_ok = True

   def name(self):
     return "Prince"
 
   def short_description(self):
     return "One player discards his or her hand"     

#############################################################################
  
class HandmaidCard(ICard):

   value = 4;
   quantity = 2;
   needs_target = False
   self_target_ok = False

   def name(self):
     return "Handmaid"
 
   def short_description(self):
     return "Protection until your next turn"

#############################################################################

class BaronCard(ICard):

   value = 3;
   quantity = 2;
   needs_target = True
   self_target_ok = False

   def name(self):
     return "Baron"
 
   def short_description(self):
     return "Compare hands; lower hand is out"

#############################################################################

class PriestCard(ICard):

   value = 2;
   quantity = 2;
   needs_target = True
   self_target_ok = False

   def name(self):
     return "Priest"
 
   def short_description(self):
     return "Look at a hand"

#############################################################################

class GuardCard(ICard):

   value = 1;
   quantity = 5;
   needs_target = True
   self_target_ok = False

   def name(self):
     return "Guard"
 
   def short_description(self):
     return "Guess a player's hand"

   def act(self, target, guess):
     if guess.value == target.hand.value:
       print target.name + " is out of the round!"
       target.alive = False;

#############################################################################

class LoserCard(ICard):

   value = 0;
   quantity = 99;

   def name(self):
     return "Loser"
 
   def short_description(self):
     return "Theoretical card, should not see this during play"

#############################################################################

class IPlayer:
  """Base class for all Players"""
  total_score = 0
  name = "DefaultName"
  hand = LoserCard()
  alive = True

  def __init__(self,name):
    self.name = name

  def take_turn(self,deck,players):
    raise NotImplementedError

  def draw_card(self,deck):
    self.hand = deck.pop()

#############################################################################

class HighRollerRandomAttacker(IPlayer):

  def take_turn(self,deck,players):
    print self.name + "\'s turn!"

    new_card = deck.pop();

    print self.name + " deciding between " + new_card.name_value() + \
            " and " + self.hand.name_value()

    play = ICard();
    if (new_card.value > self.hand.value):
      play = self.hand;
      self.hand = new_card;
    else:
      play = new_card;

    print self.name + " plays " + play.name_value();

    if play.value == 1:
      target = self.choose_random_opponent(players)
      guess = self.choose_random_non_guard()

      print self.name + " guess that " + target.name + \
                        " is holding " + guess.name()
      play.act(target, guess)

    elif play.value == 2:
      print "not implemented"
    elif play.value == 3:
      print "not implemented"
    elif play.value == 4:
      print "not implemented"
    elif play.value == 5:
      print "not implemented"
    elif play.value == 6:
      print "not implemented"
    elif play.value == 7:
      print "not implemented"

  def choose_random_opponent(self, players):
    opponents = list(players)    
    opponents.remove(self)
    shuffle(opponents)
    return opponents.pop();
  
  def choose_random_non_guard(self):
    possibilities = [PrincessCard(),  \
                     CountessCard(),  \
                     KingCard(),      \
                     PrinceCard(),    \
                     HandmaidCard(),  \
                     BaronCard(),     \
                     PriestCard()]
    shuffle(possibilities)
    return possibilities.pop()





#############################################################################

class HumanPlayer(IPlayer):

  def take_turn(self,deck,players):
    deck.pop();
    print self.name + "\'s turn!"

#############################################################################

list_of_cards = [PrincessCard(), CountessCard(), KingCard(), PrinceCard(), \
                 HandmaidCard(), BaronCard(), PriestCard(), GuardCard()]

print "~~~ List of Cards ~~~"
for c in list_of_cards:
  print c.summary()

#############################################################################
# Game setup

# Setup players
players = [HighRollerRandomAttacker("Robot1"), 
           HighRollerRandomAttacker("Robot2"), 
           HighRollerRandomAttacker("Robot3")]
shuffle(players)


# Setup and shuffle deck
deck = [PrincessCard(), \
        CountessCard(), \
        KingCard(), \
        PrinceCard(), PrinceCard(), \
        HandmaidCard(), HandmaidCard(), \
        BaronCard(), BaronCard(),\
        PriestCard(), PriestCard(), \
        GuardCard(), GuardCard(), GuardCard(), GuardCard(), GuardCard()]

shuffle(deck)

# Set aside one card
deck.pop();

# Each player draws a card
for p in players:
  p.alive = True
  p.draw_card(deck) 

#print ""
#print "~~~ Deck ~~~"
#print deck.pop().name() + " -- set aside"
#for c in deck:
#  print c.name()


#############################################################################
# Begin game

print ""
game_over = False
turn = 0;
while game_over != True:
  print "Deck size: " + str(len(deck));

  if players[turn % len(players)].alive:
    players[turn % len(players)].take_turn(deck,players);

  turn = turn + 1;

  alive_players = 0;
  for p in players: 
    if p.alive == True:
      alive_players = alive_players + 1;

  if alive_players < 2:
    game_over = True;

  if len(deck) == 0:
    game_over = True;

print ""
print "~~~ Game Over ~~~"
# Determine winner
winner = IPlayer("FakePlayer");
for p in players:
  if p.alive == True:
    print p.name  + ": " + p.hand.name_value()
    if p.hand.value > winner.hand.value:
      winner = p

print ""
print "Winner: " + winner.name + ", with the " + winner.hand.name_value()
