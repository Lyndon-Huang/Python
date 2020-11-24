#!/usr/bin/env python3
"""
Assignment 2 - UNO++
CSSE1001/7030
Semester 2, 2018
"""

import random

__author__ = "Xuannan Huang 45047257"

# Write your classes here
#super class Card
class Card():
    '''
    This class is for different cards' number and colour
    '''
    def __init__(self, number, colour):
        '''
        This method initializes the Cards' number and colour
        
        parameter:
            number (int): the number for the card
            colour(string): the colour for the card
        '''
        self._number = number
        self._colour = colour
        
    def get_number(self):
        '''
        return:
            the Cards' number
        '''
        return self._number
    
    def get_colour(self):
        '''
        return:
            the Cards' colour
        '''
        return self._colour
    
    def set_number(self, number):
        '''
        This method for setting a new number to the card
        
        parameter:
            number (int): the new number for the card
        '''
        self._number = number
        
    def set_colour(self,colour):
        '''
        This method for setting a new colour to the card
        
        parameter:
            number (int): the new colour for the card
        '''
        self._colour = colour
        
    def get_pickup_amount(self):
        '''
        The method return the number of cards
            the next player should pick up

        return 0
        '''
        return 0
    
    def matches(self, card):
        '''
        This method for making sure the player' card
            matches with the last player's card

        parameter:
            card (Card): the card 

        return:
            bool
        '''
        if self.get_colour() == card.get_colour():
            return True
        else:
            if self.get_number() == card.get_number():
                return True
            else:
                return False
    def play(self, player, game):
        '''
        This method return the special action of
            the special card in the subclass
        '''
        pass
                    
    def __str__(self):
        '''
        output the card and its number and colour
        '''
        return f'Card({self._number}, {self._colour})'

    def __repr__(self):
        '''
        output the card and its number and colour
        '''
        return f'Card({self._number}, {self._colour})'

#subclass of Card
class SkipCard(Card):
    '''
    This class is for the SkipCard
    '''
    def __init__(self, number, colour):
        '''
        This method initializes the SkipCards' number and colour

        parameter:
            number(int):the number of the SkipCard
            colour(string): the colour of the SkipCard
        '''
        self._number = number
        self._colour = colour

    def play(self, player, game):
        '''
        This method is about the special action for the SkipCard

        parameter:
            player: one of the player do the skip action
            game: This is the UNO Game in the a2_support file

        return:
            do the skip action
        '''
        game.skip()

    def matches(self, card):
        '''
        This method is to match the skipcards' colour

        parameter:
            card(Card): this card's colour is for matching

        return:
            bool
        '''
        if self._colour == card.get_colour():
            return True
        else:
            return False
        
    def __str__(self):
        '''
        output the SkipCard and its number and colour
        '''
        return f'SkipCard({self._number}, {self._colour})'
    
    def __repr__(self):
        '''
        output the SkipCard and its number and colour
        '''
        return f'SkipCard({self._number}, {self._colour})'
class ReverseCard(Card):
    '''
    This class is for the ReverseCard
    '''
    def __init__(self, number, colour):
        '''
        initialize the ReverseCards' number and colour

        parameter:
            number(int):the number of the ReverseCards
            colour(string): the colour of the ReverseCards
        '''
        self._number = number
        self._colour = colour

    def play(self, player, game):
        '''
        This method is about the special action for the ReverseCards

        parameter:
            player: one of the player do the reverse action
            game: This is the UNO Game in the a2_support file

        return:
            do the reverse action
        '''
        game.reverse()

    def matches(self, card):
        '''
        This method is to match the ReverseCards' colour

        parameter:
            card(Card): this card's colour is for matching

        return:
            bool
        '''
        if self._colour == card.get_colour():
            return True
        else:
            return False
    def __str__(self):
        '''
        output the ReverseCard and its number and colour
        '''
        return f'ReverseCard({self._number}, {self._colour})'
    
    def __repr__(self):
        '''
        output the ReverseCard and its number and colour
        '''
        return f'ReverseCard({self._number}, {self._colour})'
class Pickup2Card(Card):
    '''
    This class is for the Pickup2Card
    '''
    def __init__(self, number, colour):
        '''
        initialize the Pickup2Cards' number and colour

        parameter:
            number(int):the number of the Pickup2Cards
            colour(string): the colour of the Pickup2Cards
        '''
        self._number = number
        self._colour = colour

    def play(self, player, game):
        '''
        This method is about the special action for the Pickup2Card

        parameter:
            player: one of the player do the Pickup2Card action
            game: This is the UNO Game in the a2_support file

        return:
            do the Pickup2Card action
        '''
        game.get_turns().peak().get_deck().add_cards(
            game.pickup_pile.pick(self.get_pickup_amount()))

    def get_pickup_amount(self):
        '''
        return the number of cards player should pick
        '''
        return 2

    def matches(self, card):
        '''
        This method is to match the Pickup2Cards' colour

        parameter:
            card(Card): this card's colour is for matching

        return:
            bool
        '''
        if self._colour == card.get_colour():
            return True
        else:
            return False
    
    def __str__(self):
        '''
        output the Pickup2Card and its number and colour
        '''
        return f'Pickup2Card({self._number}, {self._colour})'
    
    def __repr__(self):
        '''
        output the Pickup2Card and its number and colour
        '''
        return f'Pickup2Card({self._number}, {self._colour})'
class Pickup4Card(Card):
    '''
    This class is for the Pickup4Card
    '''
    def __init__(self, number, colour):
        '''
        initialize the Pickup4Cards' number and colour

        parameter:
            number(int):the number of the Pickup4Cards
            colour(string): the colour of the Pickup4Cards
        '''
        self._number = number
        self._colour = colour

    
    def play(self, player, game):
        '''
        This method is about the special action for the Pickup4Card

        parameter:
            player: one of the player do the Pickup4Card action
            game: This is the UNO Game in the a2_support file

        '''
        game.get_turns().peak().get_deck().add_cards(
            game.pickup_pile.pick(self.get_pickup_amount()))

    def get_pickup_amount(self):
        '''
        return the number of cards player should pick
        '''
        return 4
    
    def matches(self, card):
        '''
        The card is Pickup4Card, so just return True
        '''
        return True

    def __str__(self):
        '''
        output the Pickup4Card and its number and colour
        '''
        return f'Pickup4Card({self._number}, {self._colour})'
    
    def __repr__(self):
        '''
        output the Pickup4Card and its number and colour
        '''
        return f'Pickup4Card({self._number}, {self._colour})'
# super class Deck
class Deck():
    '''
    This class is for creating different deck.
    '''
    def __init__(self, starting_cards=None):
        '''
        initialize the deck

        parameter:
            starting_cards(): create the list of the card
                                and default is NONE
        '''
        if starting_cards == None:
            self._cards = []
        else:
            self._cards = starting_cards
    
    def get_cards(self):
        '''
        return:
            the list of the card
        '''
        return self._cards

    def get_amount(self):
        '''
        return:
            the length of the card's list
        '''
        return len(self._cards)
    
    def shuffle(self):
        '''
        return:
            mix the order of the cards 
        '''
        return random.shuffle(self._cards)

    def pick(self, amount:int = 1):
        '''
        Take the first 'amount' of cards off the deck
            and return them.

        parameter:
            amount(int): the number of card should pick

        return:
            return the picked Cards
        '''
        picked_Card = self._cards[-amount:]
        picked_Card = picked_Card[::-1]
        del self._cards[-amount:]
        return picked_Card

    def add_card(self, card):
        '''
        add the card to the player's deck
        '''
        self._cards.append(card)

    def add_cards(self,card):
        '''
        add more cards to the player's deck
        '''
        self._cards.extend(card)

    def top(self):
        '''
        Peaks at the card on top of the deck

        return:
            the card or NONE
        '''
        if self._cards != []:
            return self._cards[-1]
        else:
            return None

    
# super class Player
class Player():
    '''
    This class is for player
    '''
    def __init__(self, name):
        '''
        initialize the player's name and create the deck

        parameter:
            name(string): save the player's name

        '''
        self._name = name
        self._deck = Deck()
        
    def get_name(self):
        '''
        return:
            the player's name
        '''
        return self._name
    
    def get_deck(self):
        '''
        return:
            the deck of player
        '''
        return self._deck
            
    def is_playable(self):
        '''
        judge whether the player is Humanplayer or not

        raise NotImplementedError
        '''
        raise NotImplementedError("is_playable to be implemented by subclasses")
        
    def has_won(self):
        '''
        check whether the deck is empty or not
            if it is empty, then return True
            else return False

        return:
            bool
        '''
        if self._deck.get_amount() == 0:
            return True
        else:
            return False
        
    def pick_card(self, putdown_pile):
        '''
        Selects a card to play from the players current deck.

        parameter:
            putdown_pile(): picked card match with
                            the top of card in the putdown_pile
                            
        raise NotImplementedError
        '''
        raise NotImplementedError("pick_card to be implemented by subclasses")
		
# subclass of Player
class HumanPlayer(Player):
    '''
    The subclass is for the ComputerPlayer
    '''
    def __init__(self,name):
        '''
        This method initializes the name of the Human player

        parameter:
            name(): save the name of the HumanPlayer
        '''
        self._name = name
        self._deck = Deck()
    def is_playable(self):
        '''
        judge whether the player is Humanplayer or not

        return:
            bool
        '''
        if self.__class__.__name__== 'HumanPlayer':
            return True
        else:
            return False

    def pick_card(self, putdown_pile):
        '''
        The Human Player only return NONE
        '''
        return None
        
class ComputerPlayer(Player):
    '''
    The subclass is for the ComputerPlayer
    '''
    def __init__(self, name):
        '''
        This method initializes the name of the computer player

        parameter:
            name(): save the name of the computer player
        '''
        self._name = name
        self._deck = Deck()
    def is_playable(self):
        '''
        judge whether the player is Humanplayer or not

        return:
            bool
        '''
        if self.__class__.__name__== 'HumanPlayer':
            return True
        else:
            return False
    def pick_card(self, putdown_pile):
        '''
        go though computerplayer' deck and
            choose the appropriate card

        parameter:
            putdown_pile(): picked card match with
                            the top of card in the putdown_pile
        return:
            if the card is appropriate, then return the card
            else return NONE
        '''
        for index in self._deck.get_cards():
            if index.matches(putdown_pile.get_cards()[-1]) == True:
                self._deck.get_cards().remove(index)
                return index
        return None
                


def main():
    print("Please run gui.py instead")


if __name__ == "__main__":
    main()

