"""
This python module contains the make_card, make_deck, shuffle, draw, deal and main functions. This madule if run, will run the
main function. The main function deals two hand with the number of cards specified by the user.

Authors: Moiz Shabbir Kapasi
"""

from colorama import init
init()
from colorama import Fore, Style #Importing the modules of colorama to use ANSI code
import random #In-built module in Python for shuffling and random selection

def make_card(rank,suit):
    """This function is responsible for creating the cards, based on their rank and suit and and creates the card tuple. 
    Takes in the rank and suit as parameters"""
    if rank > 10:
        if rank == 11:
            rankname="Jack"
            sh=" "+rankname[0]+suit[0]
            if suit == "Hearts" or suit == "Diamonds":
                sh = Fore.RED + sh + Style.RESET_ALL
            else:
                sh = Fore.BLUE + sh + Style.RESET_ALL
        if rank == 12:
            rankname="Queen"
            sh=" "+rankname[0]+suit[0]
            if suit == "Hearts" or suit == "Diamonds":
                sh = Fore.RED + sh + Style.RESET_ALL
            else:
                sh = Fore.BLUE + sh + Style.RESET_ALL
        if rank == 13:
            rankname="King"
            sh=" "+rankname[0]+suit[0]
            if suit == "Hearts" or suit == "Diamonds":
                sh = Fore.RED + sh + Style.RESET_ALL
            else:
                sh = Fore.BLUE + sh + Style.RESET_ALL
        if rank == 14:
            rankname="Ace"
            sh=" "+rankname[0]+suit[0]
            if suit == "Hearts" or suit == "Diamonds":
                sh = Fore.RED + sh + Style.RESET_ALL
            else:
                sh = Fore.BLUE + sh + Style.RESET_ALL
    else:
        if rank ==10:
            rankname = str(rank)
            sh=rankname+suit[0]
            if suit == "Hearts" or suit == "Diamonds":
                sh = Fore.RED + sh + Style.RESET_ALL
            else:
                sh = Fore.BLUE + sh + Style.RESET_ALL
        elif rank <10:
            rankname = str(rank)
            sh=" "+rankname+suit[0]
            if suit == "Hearts" or suit == "Diamonds":
                sh = Fore.RED + sh + Style.RESET_ALL
            else:
                sh = Fore.BLUE + sh + Style.RESET_ALL

    name= rankname + " of  " + suit

    return rank,suit,name,sh

def make_deck():
    """make_deck is the function responsible for creating a list which holds all the created cards, which is in this sense the deck of cards"""
    deck=[]
    suits=["Clubs","Hearts","Spades","Diamonds"]
    for x in range(2,15):
        for s in suits:
            deck.append(make_card(x,s))
    return deck

def shuffle(deck):
    """The function shuffle just uses the in-built random module and and uses
     the shufflle method for shuffling the elements in the list"""
    random.shuffle(deck)

def draw(deck, hand):
    """To move a card from the deck and adding to your hand, the function draw is needed to take that card in 
    random from the list of the shuffled deck and add only the short-hand of the card. The deck and hand parameters are
    assigned from the deal function"""
    if (len(deck) > 0 ):
        card=random.choice(deck)
        deck.remove(card)
        hand.append(card)
    else:
        return
    return hand

def deal(deck, number):
    """The function Deal function recalls the draw function twice on hand 1 and hand 2 which 
    is in a sense the two players of the game holding thier cards,
    for every card dealt, the function keeps track of how many card each player has and stops onces it reaches the number set by the user."""
    hand1=[]
    hand2=[]
    i=1
    while i<=number:
        hand1=draw(deck,hand1)
        hand2=draw(deck,hand2)
        i+=1

    return hand1,hand2

def cut(deck):
    n=len(deck)
    i=n//2
    if n <= 1:
        raise ValueError("There are no cards or only one card in the deck.")
    else:
        tophalf=deck[:(i+1)]
        bothalf=deck[(i+1):]
    return tophalf,bothalf

def main():

    """The function main creates the cards, deck, shuffles it and draws to each hand
     the user-specified number of cards by calling the functions defined above.
     If a user does not specifiy the number of cards, it will take 3 as default."""

    n=int(input("Please enter the no. of cards that is to be dealt for the two hands (Default value is 3) : ") or 3)
    my_deck=make_deck()
    shuffle(my_deck)
    hand1,hand2=deal(my_deck,n)
	
    print("\nHand 1\n")
    for i in hand1:
        print(i[3])

    print("\nHand 2\n")
    for i in hand2:
        print(i[3])

    print("\nThere are",len(my_deck),"cards remaining in the deck.")

if __name__ == "__main__": #Name guard for the test function.
    try:
        main()
    except ValueError:
        print("\nPlease enter an integer number only!")
    except TypeError:
        print("There are not enough cards. There can only be maximum of 26 cards in each hand.")
    input()
